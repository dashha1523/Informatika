# TODO решите задачу

import json
def task() -> float:
    json_data = '''
    [
        {
            "score": 0.9456152645028281,
            "weight": 1
        },
        {
            "score": 0.675,
            "weight": 2
        },
        {
            "score": 0.000,
            "weight": 0
        }
    ]
    '''
    data = json.loads(json_data)
    total = sum(item.get('score', 0) * item.get('weight', 0) for item in data)
    return round(total, 3)
print(task())