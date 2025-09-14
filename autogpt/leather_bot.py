"""Leather knowledge bot that replies to platform customer service bots."""
from __future__ import annotations

from autogpt.commands.leather_info import get_leather_info


class LeatherKnowledgeBot:
    """Simple bot offering leather related knowledge with platform specific replies."""

    PLATFORM_TEMPLATES = {
        "taobao": "淘宝客服您好！{info}",
        "douyin": "抖音客服您好！{info}",
        "xiaohongshu": "小红书客服您好！{info}",
    }

    PRODUCT_SUGGESTIONS = {
        "cowhide": "经典牛皮包，适合日常通勤",
        "sheepskin": "舒适羊皮夹克，柔软贴身",
        "care": "皮革护理油，延长使用寿命",
    }

    def respond(self, platform: str, topic: str) -> str:
        """Return leather knowledge and product suggestions for a platform.

        Args:
            platform: Name of the platform requesting information.
            topic: Leather topic to respond about.
        """
        info = get_leather_info(topic)
        product = self.PRODUCT_SUGGESTIONS.get(topic.lower())
        if product:
            info = f"{info} 推荐商品：{product}"
        template = self.PLATFORM_TEMPLATES.get(platform.lower(), "{info}")
        return template.format(info=info)
