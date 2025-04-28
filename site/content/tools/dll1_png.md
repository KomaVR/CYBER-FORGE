---
title: "dll1.png"
description: "
从一段代码阐述DllMain（从xx师傅学习来）
#include \"pch.h\"
#include <iostream>
#include <Windows.h>

extern \"C\" __declspec(dllexport) void printMessageBox()
// 导出函数，实例中运用到的dllexport用于在dll中将函数、类等申明为导出函数，供其他程序调用
// 对应的还有dllimport，用于从别的动态链接库中导入函数、类、对象等供本地动态库或者exe调用
{
   int x;
   x = MessageBoxA(GetForegroundWindow(), \"Hello World\", \"by testdll\", 1);
}

BOOL APIENTRY DllMain(HMODULE hModule, DWORD ul_reason_for_call, LPVOID lpReserved)
{
   switch (ul_reason_for_call)
   {
   case DLL_PROCESS_ATTACH:
      int x;
      x = MessageBoxA(GetForegroundWindow(), \"Dll main~\", \"chriskali\", 1);
      break;
   case DLL_THREAD_ATTACH:
   case DLL_THREAD_DETACH:
   case DLL_PROCESS_DETACH:
      break;
   }
   return TRUE;
}
下面为调用上述Dll的主程序（从一位不知名的群友学习）
#include <iostream>
#include <windows.h>
#include <tchar.h>

int main()
{
   typedef int (*_ptestprint)(); //这是一个函数指针
   typedef int (*_ptestint)(int a, int b); //带参数的函数指针

   HINSTANCE hDll = LoadLibrary(\"Dll1.dll\"); // 加载DLL
   int nError = GetLastError();
   std::cout << nError << std::endl;
   std::cout << \"[+] StartLoad\" << std::endl;
   if (hDll != NULL) // 判断是否读到了,读不到就为NULL
   {
      std::cout << \"[+] In\" << std::endl;
      _ptestprint ptest = (_ptestprint)GetProcAddress(hDll, \"printMessageBox\"); //获取dll中的函数
      ptest(); //函数调用
      FreeLibrary(hDll);
      std::cout << \"done!\" << std::endl;
   }
   else
   {
      std::cout << \"[-] Not Loaded\" << std::endl;
   }
   return 0;
}
下面的讲解基本基于上述的代码
首先，先看一下DllMain的原型（照搬）
BOOL WINAPI DllMain(
   _In_ HINSTANCE hinstDLL, // 指向自身的句柄
   _In_ DWORD fdwReason, // 调用原因
   _In_ LPVOID lpvReserved // 隐式加载和显式加载
);
运行上述的代码后，会按照如下图片执行。DllMain会在导入时优先调用，其中 DLL_PROCESS_ATTACH 十分关键，它会在首次被加载的时候运行。


"
external_category: "Miscellaneous"
---[Visit Website](https://github.com/chriskaliX/AD-Pentest-Notes/raw/master/imgs/dll1.png)

