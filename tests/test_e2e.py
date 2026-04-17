"""
Testes end-to-end do pipeline completo (Fase 6).
"""

from __future__ import annotations

from pathlib import Path

import pytest

from luanny.config import load_config
from luanny.orchestrator import run_collection


@pytest.mark.slow
def test_e2e_govbr_pipeline(tmp_path: Path):
    """
    Smoke test instanciando o pipeline completo contra o perfil @govbr.
    Testa até 3 posts e verifica a saída.
    
    Atenção: Requer .env válido com credential do Instagram.
    """
    # Sobrescreve output dir para pasta temporária no teste
    config = load_config(max_posts=3, headless=True, capture_evidence=True, output_dir=str(tmp_path))
    
    # Roda a coleta completa
    result = run_collection("govbr", config)
    
    assert result is not None
    assert result.metadata.target_profile == "govbr"
    assert result.metadata.posts_collected > 0
    assert len(result.posts) <= 3
    
    # Checa se o output dir tem o json e o report
    run_dir = list(tmp_path.glob("govbr_*"))
    assert len(run_dir) == 1
    
    output_files = [f.name for f in run_dir[0].iterdir()]
    assert "posts.json" in output_files
    assert "report.md" in output_files
    assert "evidence" in output_files
    
    # Checa se o Evidence exist para pelo menos o primeiro post
    evidence_dir = run_dir[0] / "evidence" / result.posts[0].post_id
    assert evidence_dir.exists()
    assert (evidence_dir / "page.html").exists()
    
    # Certifique-se de que nenhum post gerou erro crítico não-recuperável de auth
    # (Pode haver erro de extração parcial de alguma tag muito maluca, mas a coleta de todos não pode falhar)
    assert result.metadata.posts_collected > 0
