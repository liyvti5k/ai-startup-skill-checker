#!/usr/bin/env python3
# AI Startup Skills Demo: generate a 7-step validation plan for a startup idea.
from dataclasses import dataclass, asdict
import json

@dataclass
class SkillStep:
    name: str
    goal: str
    prompt: str

STEPS = [
    SkillStep('验证', '确认真实痛点与目标用户', '列出 3 个最痛场景，并为每个场景写出可验证假设。'),
    SkillStep('BP', '形成一页商业计划', '用问题/方案/市场/壁垒/收入五段式写一页 BP。'),
    SkillStep('政策', '识别合规与政策风险', '列出数据、隐私、行业许可相关风险及缓解措施。'),
    SkillStep('路演', '准备 3 分钟路演', '写一个 3 分钟路演稿：痛点、方案、demo、traction、ask。'),
    SkillStep('获客', '设计低成本获客实验', '提出 3 个 7 天内可执行的获客实验和成功指标。'),
    SkillStep('定价', '确定初始定价与包装', '给出 3 档定价、目标客户和每档的核心价值。'),
    SkillStep('注册', '规划公司注册与启动清单', '列出注册主体、银行、税务、合同的最小启动清单。'),
]

def build_plan(idea: str) -> dict:
    return {
        'idea': idea,
        'steps': [asdict(step) for step in STEPS],
        'next_action': '先完成第 1 步，把验证结果写回本 JSON。'
    }

def score(steps_done: int) -> str:
    pct = int(steps_done / len(STEPS) * 100)
    return '{}/{} 步完成，进度 {}%'.format(steps_done, len(STEPS), pct)

def main():
    idea = input('输入你的 AI 创业想法: ').strip() or '一个面向独立开发者的 AI 启动助手'
    plan = build_plan(idea)
    print('\n=== AI Startup Skills 七步计划 ===')
    for i, step in enumerate(plan['steps'], 1):
        print('{}. {} | {}'.format(i, step['name'], step['goal']))
        print('   Prompt: {}'.format(step['prompt']))
    done = int(input('\n已完成几步? '))
    print(score(done))
    print('\nJSON 预览:')
    print(json.dumps(plan, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()