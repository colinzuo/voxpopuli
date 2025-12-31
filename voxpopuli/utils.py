# Copyright (c) Facebook, Inc. and its affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

import os
from typing import Optional

from torch.hub import download_url_to_file
from tqdm.contrib.concurrent import process_map


def download_url(url, dst):
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    download_url_to_file(url, dst)
    

def multiprocess_run(
        a_list: list, func: callable, n_workers: Optional[int] = None
):
    process_map(func, a_list, max_workers=n_workers, chunksize=1)
