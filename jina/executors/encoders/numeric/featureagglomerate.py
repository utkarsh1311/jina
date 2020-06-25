__copyright__ = "Copyright (c) 2020 Jina AI Limited. All rights reserved."
__license__ = "Apache-2.0"

import numpy as np

from .. import BaseNumericEncoder
from ...decorators import batching


class FeatureAgglomerationEncoder(BaseNumericEncoder):
    """
    :class:`FeatureAgglomerationEncoder` encodes data from an ndarray in size `B x T` into an ndarray in size `B x D`
    https://scikit-learn.org/stable/modules/generated/sklearn.cluster.FeatureAgglomeration.html
    """

    def __init__(self,
                 output_dim: int,
                 *args,
                 **kwargs):
        """
        :param output_dim: the output size.
        """
        super().__init__(*args, **kwargs)
        self.output_dim = output_dim

    def post_init(self):
        from sklearn.cluster import FeatureAgglomeration
        self.model = FeatureAgglomeration(n_clusters=self.output_dim)

    @batching
    def encode(self, data: 'np.ndarray', *args, **kwargs) -> 'np.ndarray':
        """
        :param data: a `B x T` numpy ``ndarray``, `B` is the size of the batch
        :return: a `B x D` numpy ``ndarray``
        """
        return self.model.fit_transform(data)
