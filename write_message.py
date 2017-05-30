# coding=utf-8
import os
def make_android_java_file(resname,mod_type,mod_str,mod_param_list):
	file_name = make_class_name(resname,mod_type)
        make_android_file(file_name,resname,mod_type,mod_str,mod_param_list)
def make_android_res_file(resname,mod_type,mod_str,mod_param_list):
	file_name = make_xml_name(resname,mod_type)
	make_android_file(file_name,resname,mod_type,mod_str,mod_param_list)
def make_android_file(file_name,resname,mod_type,mod_str,mod_param_list):
        contents = ''
        with open ('%s%s%s' % ('mod_str/',mod_str,'.txt')) as file_object:
                contents = file_object.read()
        mod_str = contents%(tuple(mod_param_list))
        try:
                os.mkdir('%s%s'%('output/',resname))
        except OSError:
                print "Error: 文件名重复"
        output_path = '%s%s%s%s'%('output/',resname,"/",file_name)
        with open(output_path,'w') as file_object:
                file_object.write(mod_str)

#get layout name
def make_xml_name(res_name,mod_type):
	return '%s%s%s%s'%(mod_type,'_',res_name,".xml")
	
#get class name
def make_class_name(res_name,mod_type):
        return '%s%s%s'%(make_mod_name(res_name),mod_type,'.java')
#get replace string
def make_mod_name(res_name):
        modlist = res_name.split('_')
        modvalue=''
        for mod in modlist:
                tempmod = '%s%s'%(mod[0].upper(),mod[1:])
                modvalue='%s%s'%(modvalue,tempmod)
        return modvalue	
