import random


def process_main(count):
    player_not_change_num = 0
    player_change_num = 0
    for i in range(0, count):
        doors = [0, 0, 0]
        doors[random.randint(0, 2)] = 1  # 随机放置汽车
        # 参与者随机选择
        player = random.randint(0, 2)
        # 主持人选出山羊的门且不能与参与者选择相同
        host = random.randint(0, 2)
        while (doors[host] == 1) or (host == player):
            host = random.randint(0, 2)
        if doors[player] == 1:  # 不换中奖概率
            player_not_change_num += 1
        else:  # 换中奖
            player_change_num += 1
    return player_not_change_num / 1000, player_change_num / 1000


if __name__ == '__main__':
    not_change_winning_rate, change_winning_rate = process_main(1000)
    print('不换中奖概率：', not_change_winning_rate)
    print('换中奖概率：', change_winning_rate)
