import pandas as pd
import numpy as np
from scipy import stats

chat_id = 1251251937 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 0.09
    p_val = stats.anderson_ksamp([x, y])[2]
    return True if p_val <= alpha else False # Ваш ответ, True или False
