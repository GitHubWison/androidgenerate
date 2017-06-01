# coding=utf-8
import write_message
import os
#创建activity
def make_activity(first_str,second_str):
	mod_param_list = [first_str,second_str]
	write_message.make_android_java_file(res_name,'Activity','activitystr',mod_param_list)
#创建fragment
def make_fragment(mod_param_list):
	write_message.make_android_java_file(res_name,'Fragment','fragmentstr',mod_param_list)
#创建viewmodel
def make_viewmodel(first_str):
	mod_param_list = [first_str]
	write_message.make_android_java_file(res_name,'ViewModel','viewmodelstr',mod_param_list)
#创建layout for fragment
def make_layout(first_str):
	mod_param_list = [first_str]
	write_message.make_android_res_file(res_name,'fragment','layoutfragmentstr',mod_param_list)
#创建layout for activity
def make_layout_activity(first_str):
	mod_param_list = [first_str]
	write_message.make_android_res_file(res_name,'activity','layoutactivitystr',mod_param_list)
res_name = raw_input('input modname(split with "_"):')
modstr =write_message.make_mod_name(res_name)
make_activity(modstr,res_name)
make_fragment([modstr]*8)
make_viewmodel(modstr)
make_layout('%s%s'%(modstr,'ViewModel'))
make_layout_activity(res_name)

#将生成的文件转移到对应的文件夹中
#1.等待用户输入项目地址
project_address = raw_input('输入项目所在目录:')
java_address = raw_input('java文件的存放目录')
linux_copy_order = ''
with open ('shell/copy_to_androidpro.txt')as file_object:
	linux_copy_order = file_object.read()
linux_copy_order = linux_copy_order%(res_name,res_name,res_name,project_address,java_address,res_name,res_name,project_address)
print linux_copy_order
os.system(linux_copy_order)
