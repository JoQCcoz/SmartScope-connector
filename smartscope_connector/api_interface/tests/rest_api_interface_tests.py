import pytest
from .. import rest_api_interface as RestAPI
from smartscope_connector.Datatypes.querylist import QueryList
from smartscope_connector.models import Microscope, Detector, AtlasModel

def test_generate_get_url():
    url = RestAPI.generate_get_url(base_url='http://testurl/api', route='microscopes', filters=dict(name='fake_scope', microscope_id='h0PgRUjUq2K2Cr1CGZJq3q08il8i5n' ))
    assert url == 'http://testurl/api/microscopes/?name=fake_scope&microscope_id=h0PgRUjUq2K2Cr1CGZJq3q08il8i5n&'

def test_api_connection():
    response = RestAPI.get_from_API(url='http://nginx:80/api/')
    assert response.status_code == 200

def test_api_connection_error():
    with pytest.raises(RestAPI.RequestUnsuccessfulError):
        RestAPI.get_from_API(url='http://nginx:80/wrongapi/')

def test_get_from_API():
    import json
    response = RestAPI.get_from_API(url='http://nginx:80/api/microscopes/?name=fake_scope&')
    assert len(json.loads(response.content)['results']) == 1

def test_get_single():
    response = RestAPI.get_single(object_id='h0PgRUjUq2K2Cr1CGZJq3q08il8i5n',output_type=Microscope)
    assert isinstance(response, Microscope)
    assert response.name == 'fake_scope'
    assert response.uid == 'h0PgRUjUq2K2Cr1CGZJq3q08il8i5n'

def test_get_many():
    results = RestAPI.get_many(output_type=Detector,name='test_k2', id=3)
    assert len(results) == 1
    assert isinstance(results[0],Detector)

def test_patch_single():
    object_id = '3'
    url = f'http://nginx:80/api/detectors/{object_id}/'
    data = dict(atlas_max_tiles_X= 7)
    response = RestAPI.patch_single(url=url,data=data)
    assert response.status_code == 200
    assert response.json()['atlas_max_tiles_X'] == 7
    #Reset Value
    data = dict(atlas_max_tiles_X= 6)
    response = RestAPI.patch_single(url=url,data=data)
    assert response.json()['atlas_max_tiles_X'] == 6

def test_update():
    object_id = '3'
    instance = RestAPI.get_single(object_id=object_id,output_type=Detector)
    instance = RestAPI.update(instance=instance, atlas_max_tiles_X=7)
    assert isinstance(instance,Detector)
    assert instance.atlas_max_tiles_X == 7
    instance = RestAPI.update(instance=instance, atlas_max_tiles_X=6)
    assert instance.atlas_max_tiles_X == 6

def generate_get_single_object_for_testing():
    return Detector.model_validate(dict(name='New_test_detector', 
                                       microscope_id='h0PgRUjUq2K2Cr1CGZJq3q08il8i5n',
                                       detector_model='K2',
                                       atlas_mag=10000,
                                       atlas_max_tiles_X=6,
                                       atlas_max_tiles_Y=6,
                                       spot_size=5,
                                       c2_perc=0.5,
                                       atlas_c2_aperture=50))

def test_post():
    obj = generate_get_single_object_for_testing()
    url = f'http://nginx:80/api/detectors/'
    output = RestAPI.post(url=url,data=obj.model_dump(exclude_none=True,by_alias=True))
    assert output['id'] is not None
    assert output['name'] == 'New_test_detector'

def test_post_single():
    obj = generate_get_single_object_for_testing()
    output = RestAPI.post_single(instance=obj)
    assert isinstance(output,Detector)
    assert output.uid is not None

def test_post_many():
    objs = QueryList([generate_get_single_object_for_testing() for i in range(3)])
    output = RestAPI.post_many(instances=objs,output_type=Detector)
    assert len(output) == 3
    assert isinstance(output[0],Detector)
    assert output[0].uid is not None


def test_delete_single():
    obj = RestAPI.get_many(output_type=Detector, name='New_test_detector').first()
    response = RestAPI.delete_single(instance=obj)
    assert response.status_code == 204

def test_delete_many():
    objs = RestAPI.get_many(output_type=Detector, name='New_test_detector', all=True)
    response = RestAPI.delete_many(instances=objs)
    assert response.status_code == 204



