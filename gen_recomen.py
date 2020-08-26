# -*- coding: utf-8 -*-

# Using founded data
# import get_data

from recsys.RecSys import *

recSys = RecSys(user_data='data/sp_users_convert.json', item_data='data/sp_pois_convert.json', rating_data='data/sp_reviews_convert.json')
## Evaluates
# recSys.itemSimilarity(eval=True)
# recSys.itemSimilarity(similarityType='cosine', eval=True)
# recSys.itemSimilarity(similarityType='pearson', eval=True)

# recSys.itemContent(attributes=['item_id', 'category'], splitAttribute='category', eval=True)
# recSys.itemContent(attributes=['item_id', 'category'], eval=True)
# recSys.itemContent(attributes=['item_id', 'latitude', 'longitude'], eval=True)
# recSys.itemContent(attributes=['item_id', 'category', 'latitude', 'longitude'], splitAttribute='category', eval=True)
# recSys.itemContent(attributes=['item_id', 'category', 'latitude', 'longitude'], eval=True)
# recSys.itemContent(attributes=['item_id', 'name'], eval=True)
# recSys.itemContent(attributes=['item_id', 'name', 'category'], splitAttribute='category', eval=True)
# recSys.itemContent(attributes=['item_id', 'name', 'category'], eval=True)
# recSys.itemContent(splitAttribute='category', eval=True)
# recSys.itemContent(eval=True)

## Recommends for new users
recent_data = gl.SFrame()
recent_data['user_id'] = ['100000260748852833494']
recent_data['item_id'] = [59392558]
recent_data['rating'] = [0.8]

# recSys.itemSimilarity(similarityType='pearson', newUsers=[108096371283696583542], newObservationData=recent_data, eval=True)
#recSys.itemSimilarity(newUsers=['100003258120679643845'])

def test(user_id):
    recSys.itemSimilarity(newUsers=[user_id], newObservationData=recSys._ratings.filter_by([user_id], 'user_id'), eval=True)
# test('100048669037283425080')
# import pdb; pdb.set_trace()
#recSys.itemContent(attributes=['item_id', 'category'], newUsers=['109872608950295275568'])
recSys.itemContent(attributes=['item_id', 'category'], newUsers=['109737622095470537985'])

## Get similar items
# recSys.itemSimilarity(similarityType='pearson', similarItem=[59224731])
# recSys.itemContent(newUsers=[99999], similarItem=[59224731])
