# -*- coding: utf-8 -*-
import get_data

from recsys.RecSys import *

recSys = RecSys(user_data='data/user.json', item_data='data/poi.json', rating_data='data/review.json')
## Evaluates
recSys.itemSimilarity(eval=True)
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
recent_data['user_id'] = ['108096371283696583542']
recent_data['item_id'] = [59392558]
recent_data['rating'] = [0.8]
recSys.itemSimilarity(similarityType='pearson', newUsers=[108096371283696583542], newObservationData=recent_data, eval=True)
# recSys.itemContent(newUsers=[99999], newObservationData=recent_data)

## Get similar items
# recSys.itemSimilarity(similarityType='pearson', similarItem=[59224731])
# recSys.itemContent(newUsers=[99999], similarItem=[59224731])
