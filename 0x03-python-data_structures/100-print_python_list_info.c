#include <stdio.h>
#include <Python.h>
/**
 *print_python_list_info - Prints Python lists info on CPython
 *@p: Pointer to the PyObj
 *Return: Void
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size = PyList_Size(p);
	PyObject *obj;
	unsigned int index = 0;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", (((PyListObject *)(p))->allocated));
	while (index < size)
	{
		obj = PyList_GetItem(p, index);
		printf("Element %i: %s\n", index, Py_TYPE(obj)->tp_name);
		index++;
	}
}
