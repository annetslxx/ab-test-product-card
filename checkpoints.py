"""Необязательная помощь: подготовка каждой метрики отдельно.
Не запускать вместо заданий; преподаватель может показать нужную функцию.
"""
def prepare_arppu(participants, events):
    p = events.loc[events.event_type == 'purchase']
    result = p.groupby('user_id').revenue.sum().reset_index()
    return result.merge(participants, on='user_id', validate='one_to_one')

def prepare_conversion(participants, events):
    ids = events.loc[events.event_type == 'purchase', 'user_id'].unique()
    result = participants.copy()
    result['bought'] = result.user_id.isin(ids).astype(int)
    return result

def prepare_arpu(participants, events):
    amounts = events.loc[events.event_type == 'purchase'].groupby('user_id').revenue.sum().reset_index()
    result = participants.merge(amounts, on='user_id', how='left', validate='one_to_one')
    result['revenue'] = result.revenue.fillna(0)
    return result
