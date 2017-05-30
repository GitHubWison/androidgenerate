# coding=utf-8
import write_message
#创建activity
def make_activity(first_str,second_str):
	mod_param_list = [first_str,second_str]
	write_message.make_android_java_file(res_name,'Activity','activitystr',mod_param_list)
#创建fragment
def make_fragment(first_str):
	mod_param_list = [first_str]
	write_message.make_android_java_file(res_name,'Fragment','fragmentstr',mod_param_list)
#创建viewmodel
def make_viewmodel(first_str):
	mod_param_list = [first_str]
	write_message.make_android_java_file(res_name,'ViewModel','viewmodelstr',mod_param_list)
#创建layout
def make_layout(first_str):
	mod_param_list = [first_str]
	write_message.make_android_res_file(res_name,'layout','layoutstr',mod_param_list)
res_name = raw_input('input modname(split with "_"):')
modstr =write_message.make_mod_name(res_name)
make_activity(modstr,res_name)
make_fragment(modstr)
make_viewmodel(modstr)
make_layout('%s%s'%(modstr,'ViewModel'))
