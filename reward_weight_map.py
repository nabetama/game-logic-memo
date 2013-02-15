import random

class RewardSample():
    panel_comp_rewards = {
        # アイテム報酬
        'item': [
            {'id': '68',  'weight': 0.4},
            {'id': '78',  'weight': 0.4},
            {'id': '13',  'weight': 0.1},
            {'id': '16',  'weight': 0.05},
            {'id': '17',  'weight': 0.05},
            ],
        # カード報酬
        #'card': [
        #    {'id' : '41329', 'weight' : 1},
        #    {'id' : '51329', 'weight' : 1},
        #    {'id' : '61329', 'weight' : 1},
        #    ],
        # 確定報酬
        #'decision': [
        #    {'id': '132', 'weight': 1},# item
        #    ]
        }

    def panel_comp_reward(self, reward_type):
        """ 引数で受け取った種類の報酬をpanel_comp_rewardsから選択し,
        報酬idを文字列で返す """
        if not reward_type:
            return None
        rewards = self.panel_comp_rewards[reward_type]
        reward_ids = []
        for reward in rewards:
            reward_ids += [reward['id']] * int(reward['weight'] * 100)
        reward_id = random.choice(reward_ids)
        return reward_id
