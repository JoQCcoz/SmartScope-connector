

def reset_atlas_targets(atlas_id: str):
    from .api_interface.rest_api_interface import delete_many, get_many, update, get_single
    from .models import AtlasModel, SquareModel

    atlas = get_single(AtlasModel, atlas_id)
    squares = get_many(SquareModel, atlas_id=atlas_id, all=True)
    delete_many(squares)
    atlas = update(atlas, status='processed')

    print('Successfully deleted all targets from atlas and set status back to processed')

def test_selector_clustering():
    from .api_interface.rest_api_interface import get_many
    from .models import SquareModel
    from Smartscope.core.settings.worker import PLUGINS_FACTORY
    from Smartscope.lib.Datatypes.base_plugin import SelectorSorter
    selector = PLUGINS_FACTORY['Size selector']
    squares = get_many(output_type=SquareModel,grid_id="1grid1NU7da3oLMXBOXJZSctEKr3jg",route_suffixes=['detailed'],all=True)
    print(squares[0])
    sorter = SelectorSorter(selector, squares, n_classes=5, limits=[0, 1.0])
    sorter.classes
    sorter.labels
    for a in sorter:
        print(a)


def test_get_selectors():
    from Smartscope.core.data_manipulations import get_target_methods
    from .api_interface.rest_api_interface import get_single
    from .models import AtlasModel

    atlas = get_single(AtlasModel,'grid1_atlasY13FdGQMQBlDK0uGMQB', route_suffix='detailed')
    print(get_target_methods(atlas, 'selectors'))
    print(get_target_methods(atlas, 'finders'))
    print(get_target_methods(atlas, 'classifiers'))

def test_select_n_areas():
    from Smartscope.core.data_manipulations import select_n_areas
    from .api_interface.rest_api_interface import get_single
    from .models import AtlasModel

    atlas = get_single(AtlasModel,'grid1_atlasY13FdGQMQBlDK0uGMQB', route_suffix='detailed')
    print(select_n_areas(atlas, 5))