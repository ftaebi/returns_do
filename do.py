from typing import List, Tuple
from returns.iterables import Fold
from returns.io import IOResultE, IOSuccess

def test_func() -> IOResultE[List[int]]:
    ints = [IOSuccess(1), IOSuccess(2)]
    collected_ints: IOResultE[Tuple[int, ...]] = Fold.collect(ints, IOSuccess(()))
    return IOResultE.do(
        [x*x for x in list(col)]
        for col in collected_ints
    )
