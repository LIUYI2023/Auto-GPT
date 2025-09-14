"""Tests for LeatherKnowledgeBot."""
from autogpt.leather_bot import LeatherKnowledgeBot


def test_leather_bot_platform_response():
    bot = LeatherKnowledgeBot()
    response = bot.respond("taobao", "cowhide")
    assert "淘宝客服" in response
    assert "牛皮耐磨" in response
    assert "推荐商品：经典牛皮包" in response


def test_leather_bot_unknown_platform():
    bot = LeatherKnowledgeBot()
    response = bot.respond("unknown", "care")
    assert response == "皮革应避免潮湿，并定期使用保养油。 推荐商品：皮革护理油，延长使用寿命"
