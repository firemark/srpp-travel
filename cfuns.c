#include <Python.h>
#include <numpy/ndarrayobject.h>

struct s_placedt {
    int index;
    int cor[2];
} typedef placedt;

static PyObject* crossover_with_range(PyObject *self, PyObject *args){

    PyArrayObject *a, *b;
    int i, start, end;

    printf("wheee\n");

    if (!PyArg_ParseTuple(args, "OO(ii)", &a, &b, &start, &end))
        return NULL;

    printf("loaded tuple\n range = (%d, %d)", start, end);

    placedt *data_a = PyArray_DATA(a);
    placedt *data_b = PyArray_DATA(b);

    int len_a = PyArray_DIM(a, 0);
    int len_b = PyArray_DIM(b, 0);
    printf("len_a: %d leb_b: %d\n", len_a, len_b);

    for(i=0; i < len_a; i++){
        printf("%d: %d, %d\n", i, data_a[i*2].index, data_b[i*2].index);
    }

    Py_INCREF(Py_None);
    return Py_None;
}

static PyMethodDef methods[] = {
    {"crossover_with_range", crossover_with_range, METH_VARARGS, ""},
    {NULL}
};

PyMODINIT_FUNC
initcfuns(void){
    (void) Py_InitModule("cfuns", methods);
}

int main(int argc, char *argv[]){
    Py_SetProgramName(argv[0]);
    Py_Initialize();
    initcfuns();
}