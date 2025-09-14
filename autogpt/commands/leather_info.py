"""Leather knowledge commands for the leather bot."""
from __future__ import annotations

from autogpt.commands.command import command

LEATHER_KNOWLEDGE = {
    "cowhide": "牛皮耐磨，常用于皮鞋和皮包。",
    "sheepskin": "羊皮柔软，适合制作服装。",
    "care": "皮革应避免潮湿，并定期使用保养油。",
}


@command("get_leather_info", "Get leather info", '"topic": "<topic>"')
def get_leather_info(topic: str) -> str:
    """Return knowledge about a specific leather topic.

    Args:
        topic: Topic to search in the leather knowledge base.
    """
    return LEATHER_KNOWLEDGE.get(topic.lower(), "暂无该皮革主题的相关知识。")
