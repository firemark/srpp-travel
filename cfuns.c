#include <Python.h>
#include <numpy/ndarrayobject.h>
#include <string.h>

const int find_gen(const int *genes, const int seeked_gen, const int len, const int size){
    int i;
    for(i=0; i < len; i+=size)
        if(genes[i] == seeked_gen)
            return 1;
    return 0;
}

const void find_empty_and_change(const int *genes, const int *gen_ptr, const int len, const int size){
    int i=0;
    for(i=0; i < len; i+=size){
        if (genes[i] == -1){
            memcpy(&genes[i], gen_ptr, size*sizeof(int));
            return;
        }
    }
}

static PyObject* crossover_fill(PyObject *self, PyObject *args){

    PyArrayObject *obj_child, *obj_parent;
    int i, j;

    if (!PyArg_ParseTuple(args, "OO", &obj_child, &obj_parent))
        return NULL;

    //placedt has 3 ints
    const int *child = PyArray_DATA(obj_child);
    const int *parent = PyArray_DATA(obj_parent);
    const int size = PyArray_ITEMSIZE(obj_child) / sizeof(int);
    const int len = PyArray_DIM(obj_child, 0) * size;

    for(i=0; i < len; i+=size)
        if(!find_gen(child, parent[i], len, size))
            find_empty_and_change(child, &parent[i], len, size);

    Py_INCREF(Py_None);
    return Py_None;
}

static PyMethodDef methods[] = {
    {"crossover_fill", crossover_fill, METH_VARARGS, ""},
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