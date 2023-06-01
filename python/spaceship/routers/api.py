from fastapi import APIRouter
import numpy as np

router = APIRouter()


@router.get('')
def hello_world() -> dict:
    return {'msg': 'Hello, World!'}

@router.get('/matrix_mult')
def matrix() -> dict:
    matrix_a = np.random.rand(10, 10).tolist()
    matrix_b = np.random.rand(10, 10).tolist()
    sum = np.dot(matrix_a, matrix_b).tolist()
    result = {"matrix_a": matrix_a, "matrix_b": matrix_b, "total": sum}
    return result
