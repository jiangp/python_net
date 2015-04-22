/*************************************************************************
	> File Name: testCtypes.c
	> Author: Arwen
	> Mail:745529725@qq.com 
	> Created Time: Tue 21 Apr 2015 05:56:52 PM CST
 ************************************************************************/

#include<stdio.h>
#include<stdlib.h>
#include<Python.h>
int run_nasl()
{
	Py_Initialize();
	PyRun_SimpleString("import sys");
	PyRun_SimpleString("sys.path.append('./')");
	PyObject * pModule = NULL;
	PyObject * pFunc = NULL;
	pModule = PyImport_ImportModule("ctypes");
	pFunc = PyObject_GetAttrString(pModule, "hello");
	PyEval_CallObject(pFunc, NULL);

	Py_Finalize();

	return 0;

}
