from __future__ import absolute_import, division, print_function

from glue.utils import defer_draw, decorate_all_methods
from glue.viewers.histogram.layer_artist import HistogramLayerArtist
from glue.viewers.histogram.state import HistogramViewerState
from glue.viewers.histogram.viewer import MatplotlibHistogramMixin

from .base import MatplotlibJupyterViewer

__all__ = ['HistogramJupyterViewer']


@decorate_all_methods(defer_draw)
class HistogramJupyterViewer(MatplotlibHistogramMixin, MatplotlibJupyterViewer):

    LABEL = '1D Histogram'

    _state_cls = HistogramViewerState
    _data_artist_cls = HistogramLayerArtist
    _subset_artist_cls = HistogramLayerArtist

    def __init__(self, session, parent=None, state=None):
        super(HistogramJupyterViewer, self).__init__(session, parent=parent, state=state)
        MatplotlibHistogramMixin.setup_callbacks(self)
