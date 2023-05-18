#include <Python.h>

/**
 * print_python_list - prints python list info
 * @p: python object
 */

void print_python_list(PyObject *p) {
    Py_ssize_t size = PyList_Size(p);
    Py_ssize_t i;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++) {
        printf("Element %zd: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
    }
}

/**
 * print_python_bytes - prints the sizes of pyObjects
 * @p: python object in question
 */

void print_python_bytes(PyObject *p) {
    Py_ssize_t size;
    char *str;
    int i;

    printf("[.] bytes object info\n");

    if (!PyBytes_Check(p)) {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    str = PyBytes_AsString(p);

    printf("  size: %zd\n", size);
    printf("  trying string: %s\n", str);

    if (size > 10)
        size = 10;

    printf("  first %zd bytes: ", size);
    for (i = 0; i < size; i++)
        printf("%02x%c", (unsigned char)str[i], (i < size - 1) ? ' ' : '\n');
}

