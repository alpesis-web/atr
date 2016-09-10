import json

from acceptance_tests.mixins.apiservertestmixins import APIServerTestMixin

class APIDreamsTests(APIServerTestMixin):

    def test_post(self):
        dream1 = self._create_data('hiking')
        self.assertEquals(dream1['dream'], 'hiking')
        self.assertEquals(dream1['completed'], False)

        dream2 = self._create_data('dancing', completed=True)
        self.assertEquals(dream2['dream'], 'dancing')
        self.assertEquals(dream2['completed'], True)

        assert dream1['id'] != dream2['id']


    def test_get(self):
        dream1 = self._create_data('hiking')
        dream2 = self._create_data('dancing', completed=True)
       
        get_dream1 = self._get_data(dream1['id'])
        get_dream2 = self._get_data(dream2['id']) 
        
        self.assertEquals(dream1, get_dream1)
        self.assertEquals(dream2, get_dream2)

        get_dream3 = self._get_data(dream2['id'] + 1)
        self.assertEquals(None, get_dream3)


    def test_update(self):
        dream = self._create_data('hiking')
        id = dream['id']

        updates = dict(**dream)
        updates['completed'] = True
        updates['dream'] = 'hiking hiking'

        request = self.client.put('/api/v0/dreams/%d' % id,
                                  data=json.dumps(updates),
                                  content_type='application/json')
        updated = json.loads(request.data)        

        self.assertEquals(updated, updates)
        self.assertEquals(self._get_data(id), updates)

    def test_delete(self):
        dream = self._create_data('hiking')
        id = dream['id']
        self.assertEquals(self._get_data(id), dream)

        self.client.delete('/api/v0/dreams/%d' % id)
        self.assertEquals(self._get_data(id), None)


    def _create_data(self, dream, completed=False):

        data = {
                   'dream': dream,
                   'completed': completed
               }

        response = self.client.post('/api/v0/dreams',
                                    data=json.dumps(data),
                                    content_type='application/json')
        responsed_data = json.loads(response.data)

        assert 'id' in responsed_data
        self.assertEquals(responsed_data['dream'], dream)
        self.assertEquals(responsed_data['completed'], completed)

        return responsed_data

    def _get_data(self, id):
        response = self.client.get('/api/v0/dreams/%d' % id,
                                   content_type='application/json')

        if response.status_code != 200:
            self.assertEquals(response.status_code, 404)
            return None

        return json.loads(response.data)
