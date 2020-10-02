Node: afni
==========


 Hierarchy : _tshifter3
 Exec ID : _tshifter3


Original Inputs
---------------


* args : <undefined>
* environ : {}
* ignore : <undefined>
* in_file : /scratch/pvier002/mattfeld_2020/psb6351workdir/sub-021/psb6351_wf/volreg/mapflow/_volreg3/sub-021_task-study_run-4_bold_volreg.nii.gz
* interp : Fourier
* num_threads : 1
* out_file : <undefined>
* outputtype : NIFTI_GZ
* rlt : <undefined>
* rltplus : <undefined>
* slice_encoding_direction : k
* slice_timing : [1.265, 0.0, 0.87, 0.08, 0.95, 0.16, 1.03, 0.2375, 1.1075, 0.3175, 1.1875, 0.475, 1.345, 0.555, 1.425, 0.6325, 1.5025, 0.7125, 1.5825, 0.7925, 1.6625, 0.3975, 1.265, 0.0, 0.87, 0.08, 0.95, 0.16, 1.03, 0.2375, 1.1075, 0.3175, 1.1875, 0.475, 1.345, 0.555, 1.425, 0.6325, 1.5025, 0.7125, 1.5825, 0.7925, 1.6625, 0.3975, 1.265, 0.0, 0.87, 0.08, 0.95, 0.16, 1.03, 0.2375, 1.1075, 0.3175, 1.1875, 0.475, 1.345, 0.555, 1.425, 0.6325, 1.5025, 0.7125, 1.5825, 0.7925, 1.6625, 0.3975]
* tpattern : <undefined>
* tr : 1.76
* tslice : <undefined>
* tzero : <undefined>

Execution Inputs
----------------


* args : <undefined>
* environ : {}
* ignore : <undefined>
* in_file : /scratch/pvier002/mattfeld_2020/psb6351workdir/sub-021/psb6351_wf/tshifter/mapflow/_tshifter3/sub-021_task-study_run-4_bold_volreg.nii.gz
* interp : Fourier
* num_threads : 1
* out_file : <undefined>
* outputtype : NIFTI_GZ
* rlt : <undefined>
* rltplus : <undefined>
* slice_encoding_direction : k
* slice_timing : [1.265, 0.0, 0.87, 0.08, 0.95, 0.16, 1.03, 0.2375, 1.1075, 0.3175, 1.1875, 0.475, 1.345, 0.555, 1.425, 0.6325, 1.5025, 0.7125, 1.5825, 0.7925, 1.6625, 0.3975, 1.265, 0.0, 0.87, 0.08, 0.95, 0.16, 1.03, 0.2375, 1.1075, 0.3175, 1.1875, 0.475, 1.345, 0.555, 1.425, 0.6325, 1.5025, 0.7125, 1.5825, 0.7925, 1.6625, 0.3975, 1.265, 0.0, 0.87, 0.08, 0.95, 0.16, 1.03, 0.2375, 1.1075, 0.3175, 1.1875, 0.475, 1.345, 0.555, 1.425, 0.6325, 1.5025, 0.7125, 1.5825, 0.7925, 1.6625, 0.3975]
* tpattern : <undefined>
* tr : 1.76
* tslice : <undefined>
* tzero : <undefined>


Execution Outputs
-----------------


* out_file : /scratch/pvier002/mattfeld_2020/psb6351workdir/sub-021/psb6351_wf/tshifter/mapflow/_tshifter3/sub-021_task-study_run-4_bold_volreg_tshift.nii.gz
* timing_file : <undefined>


Runtime info
------------


* command : 3dTshift -Fourier -prefix sub-021_task-study_run-4_bold_volreg_tshift.nii.gz -tpattern @slice_timing.1D -TR 1.76 /scratch/pvier002/mattfeld_2020/psb6351workdir/sub-021/psb6351_wf/tshifter/mapflow/_tshifter3/sub-021_task-study_run-4_bold_volreg.nii.gz
* duration : 60.507515
* hostname : v001
* prev_wd : /scratch/pvier002/mattfeld_2020/code
* working_dir : /scratch/pvier002/mattfeld_2020/psb6351workdir/sub-021/psb6351_wf/tshifter/mapflow/_tshifter3


Terminal output
~~~~~~~~~~~~~~~


 s
 t
 d
 e
 r
 r
  
 2
 0
 2
 0
 -
 1
 0
 -
 0
 1
 T
 2
 1
 :
 0
 0
 :
 3
 4
 .
 0
 7
 6
 2
 2
 0
 :
 +
 +
  
 3
 d
 T
 s
 h
 i
 f
 t
 :
  
 A
 F
 N
 I
  
 v
 e
 r
 s
 i
 o
 n
 =
 A
 F
 N
 I
 _
 1
 6
 .
 3
 .
 1
 8
  
 (
 D
 e
 c
  
 2
 2
  
 2
 0
 1
 6
 )
  
 [
 6
 4
 -
 b
 i
 t
 ]
 

 s
 t
 d
 e
 r
 r
  
 2
 0
 2
 0
 -
 1
 0
 -
 0
 1
 T
 2
 1
 :
 0
 0
 :
 3
 4
 .
 1
 3
 1
 6
 2
 8
 :
 
 [
 7
 m
 *
 +
  
 W
 A
 R
 N
 I
 N
 G
 :
 
 [
 0
 m
  
  
  
 I
 f
  
 y
 o
 u
  
 a
 r
 e
  
 p
 e
 r
 f
 o
 r
 m
 i
 n
 g
  
 s
 p
 a
 t
 i
 a
 l
  
 t
 r
 a
 n
 s
 f
 o
 r
 m
 a
 t
 i
 o
 n
 s
  
 o
 n
  
 a
 n
  
 o
 b
 l
 i
 q
 u
 e
  
 d
 s
 e
 t
 ,
  
 

 s
 t
 d
 e
 r
 r
  
 2
 0
 2
 0
 -
 1
 0
 -
 0
 1
 T
 2
 1
 :
 0
 0
 :
 3
 4
 .
 1
 3
 1
 6
 2
 8
 :
  
  
  
  
  
 3
 d
 W
 a
 r
 p
  
 -
 d
 e
 o
 b
 l
 i
 q
 u
 e
  
 

 s
 t
 d
 e
 r
 r
  
 2
 0
 2
 0
 -
 1
 0
 -
 0
 1
 T
 2
 1
 :
 0
 0
 :
 3
 4
 .
 1
 3
 1
 6
 2
 8
 :
  
  
 o
 n
  
 t
 h
 i
 s
  
 a
 n
 d
  
  
 o
 t
 h
 e
 r
  
 o
 b
 l
 i
 q
 u
 e
  
 d
 a
 t
 a
 s
 e
 t
 s
  
 i
 n
  
 t
 h
 e
  
 s
 a
 m
 e
  
 s
 e
 s
 s
 i
 o
 n
 .
 

 s
 t
 d
 e
 r
 r
  
 2
 0
 2
 0
 -
 1
 0
 -
 0
 1
 T
 2
 1
 :
 0
 0
 :
 3
 4
 .
 1
 3
 1
 6
 2
 8
 :
  
  
 o
 r
  
 v
 i
 e
 w
 i
 n
 g
 /
 c
 o
 m
 b
 i
 n
 i
 n
 g
  
 i
 t
  
 w
 i
 t
 h
  
 v
 o
 l
 u
 m
 e
 s
  
 o
 f
  
 d
 i
 f
 f
 e
 r
 i
 n
 g
  
 o
 b
 l
 i
 q
 u
 i
 t
 y
 ,
 

 s
 t
 d
 e
 r
 r
  
 2
 0
 2
 0
 -
 1
 0
 -
 0
 1
 T
 2
 1
 :
 0
 0
 :
 3
 4
 .
 1
 3
 1
 6
 2
 8
 :
  
  
 s
 u
 c
 h
  
 a
 s
  
 /
 s
 c
 r
 a
 t
 c
 h
 /
 p
 v
 i
 e
 r
 0
 0
 2
 /
 m
 a
 t
 t
 f
 e
 l
 d
 _
 2
 0
 2
 0
 /
 p
 s
 b
 6
 3
 5
 1
 w
 o
 r
 k
 d
 i
 r
 /
 s
 u
 b
 -
 0
 2
 1
 /
 p
 s
 b
 6
 3
 5
 1
 _
 w
 f
 /
 t
 s
 h
 i
 f
 t
 e
 r
 /
 m
 a
 p
 f
 l
 o
 w
 /
 _
 t
 s
 h
 i
 f
 t
 e
 r
 3
 /
 s
 u
 b
 -
 0
 2
 1
 _
 t
 a
 s
 k
 -
 s
 t
 u
 d
 y
 _
 r
 u
 n
 -
 4
 _
 b
 o
 l
 d
 _
 v
 o
 l
 r
 e
 g
 .
 n
 i
 i
 .
 g
 z
 ,
 

 s
 t
 d
 e
 r
 r
  
 2
 0
 2
 0
 -
 1
 0
 -
 0
 1
 T
 2
 1
 :
 0
 0
 :
 3
 4
 .
 1
 3
 1
 6
 2
 8
 :
  
  
 y
 o
 u
  
 s
 h
 o
 u
 l
 d
  
 c
 o
 n
 s
 i
 d
 e
 r
  
 r
 u
 n
 n
 i
 n
 g
 :
  
 

 s
 t
 d
 e
 r
 r
  
 2
 0
 2
 0
 -
 1
 0
 -
 0
 1
 T
 2
 1
 :
 0
 0
 :
 3
 4
 .
 1
 3
 1
 6
 2
 8
 :
  
 S
 e
 e
  
 3
 d
 W
 a
 r
 p
  
 -
 h
 e
 l
 p
  
 f
 o
 r
  
 d
 e
 t
 a
 i
 l
 s
 .
 

 s
 t
 d
 e
 r
 r
  
 2
 0
 2
 0
 -
 1
 0
 -
 0
 1
 T
 2
 1
 :
 0
 0
 :
 3
 4
 .
 1
 9
 3
 6
 1
 7
 :
 +
 +
  
 O
 b
 l
 i
 q
 u
 e
  
 d
 a
 t
 a
 s
 e
 t
 :
 /
 s
 c
 r
 a
 t
 c
 h
 /
 p
 v
 i
 e
 r
 0
 0
 2
 /
 m
 a
 t
 t
 f
 e
 l
 d
 _
 2
 0
 2
 0
 /
 p
 s
 b
 6
 3
 5
 1
 w
 o
 r
 k
 d
 i
 r
 /
 s
 u
 b
 -
 0
 2
 1
 /
 p
 s
 b
 6
 3
 5
 1
 _
 w
 f
 /
 t
 s
 h
 i
 f
 t
 e
 r
 /
 m
 a
 p
 f
 l
 o
 w
 /
 _
 t
 s
 h
 i
 f
 t
 e
 r
 3
 /
 s
 u
 b
 -
 0
 2
 1
 _
 t
 a
 s
 k
 -
 s
 t
 u
 d
 y
 _
 r
 u
 n
 -
 4
 _
 b
 o
 l
 d
 _
 v
 o
 l
 r
 e
 g
 .
 n
 i
 i
 .
 g
 z
  
 i
 s
  
 3
 0
 .
 0
 0
 0
 0
 0
 2
  
 d
 e
 g
 r
 e
 e
 s
  
 f
 r
 o
 m
  
 p
 l
 u
 m
 b
 .


Terminal - standard output
~~~~~~~~~~~~~~~~~~~~~~~~~~





Terminal - standard error
~~~~~~~~~~~~~~~~~~~~~~~~~


 +
 +
  
 3
 d
 T
 s
 h
 i
 f
 t
 :
  
 A
 F
 N
 I
  
 v
 e
 r
 s
 i
 o
 n
 =
 A
 F
 N
 I
 _
 1
 6
 .
 3
 .
 1
 8
  
 (
 D
 e
 c
  
 2
 2
  
 2
 0
 1
 6
 )
  
 [
 6
 4
 -
 b
 i
 t
 ]
 

 
 [
 7
 m
 *
 +
  
 W
 A
 R
 N
 I
 N
 G
 :
 
 [
 0
 m
  
  
  
 I
 f
  
 y
 o
 u
  
 a
 r
 e
  
 p
 e
 r
 f
 o
 r
 m
 i
 n
 g
  
 s
 p
 a
 t
 i
 a
 l
  
 t
 r
 a
 n
 s
 f
 o
 r
 m
 a
 t
 i
 o
 n
 s
  
 o
 n
  
 a
 n
  
 o
 b
 l
 i
 q
 u
 e
  
 d
 s
 e
 t
 ,
  
 

  
  
 s
 u
 c
 h
  
 a
 s
  
 /
 s
 c
 r
 a
 t
 c
 h
 /
 p
 v
 i
 e
 r
 0
 0
 2
 /
 m
 a
 t
 t
 f
 e
 l
 d
 _
 2
 0
 2
 0
 /
 p
 s
 b
 6
 3
 5
 1
 w
 o
 r
 k
 d
 i
 r
 /
 s
 u
 b
 -
 0
 2
 1
 /
 p
 s
 b
 6
 3
 5
 1
 _
 w
 f
 /
 t
 s
 h
 i
 f
 t
 e
 r
 /
 m
 a
 p
 f
 l
 o
 w
 /
 _
 t
 s
 h
 i
 f
 t
 e
 r
 3
 /
 s
 u
 b
 -
 0
 2
 1
 _
 t
 a
 s
 k
 -
 s
 t
 u
 d
 y
 _
 r
 u
 n
 -
 4
 _
 b
 o
 l
 d
 _
 v
 o
 l
 r
 e
 g
 .
 n
 i
 i
 .
 g
 z
 ,
 

  
  
 o
 r
  
 v
 i
 e
 w
 i
 n
 g
 /
 c
 o
 m
 b
 i
 n
 i
 n
 g
  
 i
 t
  
 w
 i
 t
 h
  
 v
 o
 l
 u
 m
 e
 s
  
 o
 f
  
 d
 i
 f
 f
 e
 r
 i
 n
 g
  
 o
 b
 l
 i
 q
 u
 i
 t
 y
 ,
 

  
  
 y
 o
 u
  
 s
 h
 o
 u
 l
 d
  
 c
 o
 n
 s
 i
 d
 e
 r
  
 r
 u
 n
 n
 i
 n
 g
 :
  
 

  
  
  
  
  
 3
 d
 W
 a
 r
 p
  
 -
 d
 e
 o
 b
 l
 i
 q
 u
 e
  
 

  
  
 o
 n
  
 t
 h
 i
 s
  
 a
 n
 d
  
  
 o
 t
 h
 e
 r
  
 o
 b
 l
 i
 q
 u
 e
  
 d
 a
 t
 a
 s
 e
 t
 s
  
 i
 n
  
 t
 h
 e
  
 s
 a
 m
 e
  
 s
 e
 s
 s
 i
 o
 n
 .
 

  
 S
 e
 e
  
 3
 d
 W
 a
 r
 p
  
 -
 h
 e
 l
 p
  
 f
 o
 r
  
 d
 e
 t
 a
 i
 l
 s
 .
 

 +
 +
  
 O
 b
 l
 i
 q
 u
 e
  
 d
 a
 t
 a
 s
 e
 t
 :
 /
 s
 c
 r
 a
 t
 c
 h
 /
 p
 v
 i
 e
 r
 0
 0
 2
 /
 m
 a
 t
 t
 f
 e
 l
 d
 _
 2
 0
 2
 0
 /
 p
 s
 b
 6
 3
 5
 1
 w
 o
 r
 k
 d
 i
 r
 /
 s
 u
 b
 -
 0
 2
 1
 /
 p
 s
 b
 6
 3
 5
 1
 _
 w
 f
 /
 t
 s
 h
 i
 f
 t
 e
 r
 /
 m
 a
 p
 f
 l
 o
 w
 /
 _
 t
 s
 h
 i
 f
 t
 e
 r
 3
 /
 s
 u
 b
 -
 0
 2
 1
 _
 t
 a
 s
 k
 -
 s
 t
 u
 d
 y
 _
 r
 u
 n
 -
 4
 _
 b
 o
 l
 d
 _
 v
 o
 l
 r
 e
 g
 .
 n
 i
 i
 .
 g
 z
  
 i
 s
  
 3
 0
 .
 0
 0
 0
 0
 0
 2
  
 d
 e
 g
 r
 e
 e
 s
  
 f
 r
 o
 m
  
 p
 l
 u
 m
 b
 .


Environment
~~~~~~~~~~~


* AFNI_FLOATSCAN : YES
* BASH_ENV : /home/share/Modules/4.1.3/init/bash
* BASH_FUNC__moduleraw() : () {  unset _mlre _mlIFS _mlshdbg;
 if [ "${MODULES_SILENT_SHELL_DEBUG:-0}" = '1' ]; then
 case "$-" in 
 *v*x*)
 set +vx;
 _mlshdbg='vx'
 ;;
 *v*)
 set +v;
 _mlshdbg='v'
 ;;
 *x*)
 set +x;
 _mlshdbg='x'
 ;;
 *)
 _mlshdbg=''
 ;;
 esac;
 fi;
 if [ -n "${IFS+x}" ]; then
 _mlIFS=$IFS;
 fi;
 IFS=' ';
 for _mlv in ${MODULES_RUN_QUARANTINE:-};
 do
 if [ "${_mlv}" = "${_mlv##*[!A-Za-z0-9_]}" -a "${_mlv}" = "${_mlv#[0-9]}" ]; then
 if [ -n "`eval 'echo ${'$_mlv'+x}'`" ]; then
 _mlre="${_mlre:-}${_mlv}_modquar='`eval 'echo ${'$_mlv'}'`' ";
 fi;
 _mlrv="MODULES_RUNENV_${_mlv}";
 _mlre="${_mlre:-}${_mlv}='`eval 'echo ${'$_mlrv':-}'`' ";
 fi;
 done;
 if [ -n "${_mlre:-}" ]; then
 eval `eval ${_mlre}/usr/bin/tclsh /home/share/Modules/4.1.3/libexec/modulecmd.tcl bash '"$@"'`;
 else
 eval `/usr/bin/tclsh /home/share/Modules/4.1.3/libexec/modulecmd.tcl bash "$@"`;
 fi;
 _mlstatus=$?;
 if [ -n "${_mlIFS+x}" ]; then
 IFS=$_mlIFS;
 else
 unset IFS;
 fi;
 if [ -n "${_mlshdbg:-}" ]; then
 set -$_mlshdbg;
 fi;
 unset _mlre _mlv _mlrv _mlIFS _mlshdbg;
 return $_mlstatus
}
* BASH_FUNC_create_passwd() : () {  tr -cd 'a-zA-Z0-9' < /dev/urandom 2> /dev/null | head -c${1:-8}
}
* BASH_FUNC_find_port() : () {  local host="${1:-localhost}";
 local port=$(random_number "${2:-2000}" "${3:-65535}");
 while port_used "${host}:${port}"; do
 port=$(random_number "${2:-2000}" "${3:-65535}");
 done;
 echo "${port}"
}
* BASH_FUNC_module() : () {  _moduleraw "$@" 2>&1
}
* BASH_FUNC_port_used() : () {  local port="${1#*:}";
 local host=$((expr "${1}" : '\(.*\):' || echo "localhost") | awk 'END{print $NF}');
 nc -w 2 "${host}" "${port}" < /dev/null &>/dev/null
}
* BASH_FUNC_random_number() : () {  shuf -i ${1}-${2} -n 1
}
* BASH_FUNC_source_helpers() : () {  function random_number () 
 { 
 shuf -i ${1}-${2} -n 1
 };
 export -f random_number;
 function port_used () 
 { 
 local port="${1#*:}";
 local host=$((expr "${1}" : '\(.*\):' || echo "localhost") | awk 'END{print $NF}');
 nc -w 2 "${host}" "${port}" < /dev/null &>/dev/null
 };
 export -f port_used;
 function find_port () 
 { 
 local host="${1:-localhost}";
 local port=$(random_number "${2:-2000}" "${3:-65535}");
 while port_used "${host}:${port}"; do
 port=$(random_number "${2:-2000}" "${3:-65535}");
 done;
 echo "${port}"
 };
 export -f find_port;
 function wait_until_port_used () 
 { 
 local port="${1}";
 local time="${2:-30}";
 for ((i=1; i<=time*2; i++))
 do
 if port_used "${port}"; then
 return 0;
 fi;
 sleep 0.5;
 done;
 return 1
 };
 export -f wait_until_port_used;
 function create_passwd () 
 { 
 tr -cd 'a-zA-Z0-9' < /dev/urandom 2> /dev/null | head -c${1:-8}
 };
 export -f create_passwd
}
* BASH_FUNC_switchml() : () {  typeset swfound=1;
 if [ "${MODULES_USE_COMPAT_VERSION:-0}" = '1' ]; then
 typeset swname='main';
 if [ -e /home/share/Modules/4.1.3/libexec/modulecmd.tcl ]; then
 typeset swfound=0;
 unset MODULES_USE_COMPAT_VERSION;
 fi;
 else
 typeset swname='compatibility';
 if [ -e /home/share/Modules/4.1.3/libexec/modulecmd-compat ]; then
 typeset swfound=0;
 MODULES_USE_COMPAT_VERSION=1;
 export MODULES_USE_COMPAT_VERSION;
 fi;
 fi;
 if [ $swfound -eq 0 ]; then
 echo "Switching to Modules $swname version";
 source /home/share/Modules/4.1.3/init/bash;
 else
 echo "Cannot switch to Modules $swname version, command not found";
 return 1;
 fi
}
* BASH_FUNC_wait_until_port_used() : () {  local port="${1}";
 local time="${2:-30}";
 for ((i=1; i<=time*2; i++))
 do
 if port_used "${port}"; then
 return 0;
 fi;
 sleep 0.5;
 done;
 return 1
}
* CLICOLOR : 1
* COLORTERM : truecolor
* CONDA_DEFAULT_ENV : /home/data/nbc/nbclab-env/env-py3
* CONDA_PATH_BACKUP : /home/applications/dcm2niix/build/bin:/home/applications/afni/abin:/home/applications/miniconda2.7/4.2.12/miniconda2/bin:/home/applications/mricron:/home/applications/spm12/canonical/:/home/applications/matlab/2013b/front/bin:/home/applications/freesurfer_dcnlab/bin:/home/applications/freesurfer_dcnlab/mni/bin:/home/applications/ANTs/1.9.4/bin:/home/applications/fsl/5.0.10/bin:/home/applications/fsl/5.0.10/etc:/home/applications/python/2.7.5/bin:/home/applications/cuda/5.5/bin:/opt/TurboVNC/bin:/home/share/Modules/4.1.3/bin:/usr/local/bin:/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/home/share/bin/:/bin/:/opt/ibutils/bin:/home/pvier002/bin:/home/share/bin/:/bin/
* CONDA_PREFIX : /home/data/nbc/nbclab-env/env-py3
* CONDA_PS1_BACKUP : \[\e[1;37m\e[44m\]\[\e[0;0m\]\[\e[1;39m\]\u@\h:\W$\[\e[0m\] 
* CPATH : /home/applications/cuda/5.5/include
* CPATH_modshare : /home/applications/cuda/5.5/include:1
* CUDA_BINDIR : /home/applications/cuda/5.5/bin
* CUDA_HOME : /home/applications/cuda/5.5
* CUDA_LIBDIR : /home/applications/cuda/5.5/lib
* CUDA_PATH : /home/applications/cuda/5.5
* DBUS_SESSION_BUS_ADDRESS : unix:abstract=/tmp/dbus-yHI8BHOpzn,guid=0f6eac10ef6f3e753aa2376b5f766d21
* DISPLAY : :10.0
* ENV : /home/share/Modules/4.1.3/init/profile.sh
* ENVIRONMENT : BATCH
* FREESURFER_HOME : /home/applications/freesurfer_dcnlab
* FSFAST_HOME : /home/applications/freesurfer_dcnlab/fsfast
* FSLDIR : /home/applications/fsl/5.0.10
* FSLGECUDAQ : cuda.q
* FSLLOCKDIR : 
* FSLMACHINELIST : 
* FSLMULTIFILEQUIT : TRUE
* FSLOUTPUTTYPE : NIFTI_GZ
* FSLREMOTECALL : 
* FSLTCLSH : /home/applications/fsl/5.0.10/bin/fsltclsh
* FSLWISH : /home/applications/fsl/5.0.10/bin/fslwish
* FUNCTIONALS_DIR : /home/applications/freesurfer_dcnlab/sessions
* GIT_PAGER : cat
* GNOME_TERMINAL_SCREEN : /org/gnome/Terminal/screen/62a21e44_0c74_4d12_8820_4cd3ea2bfc70
* GNOME_TERMINAL_SERVICE : :1.53
* HISTCONTROL : ignoredups
* HISTSIZE : 1000
* HOME : /home/pvier002
* HOSTNAME : v001
* ITK_GLOBAL_DEFAULT_NUMBER_OF_THREADS : 1
* JPY_PARENT_PID : 12282
* KERNEL_LAUNCH_TIMEOUT : 40
* LANG : en_US.UTF-8
* LD_LIBRARY_PATH : /home/X11copies:/home/applications/fsl/5.0.10/lib:/home/applications/python/2.7.5/lib:/home/applications/cuda/5.5/lib64:/home/applications/cuda/5.5/lib
* LD_LIBRARY_PATH_modshare : /home/X11copies:2:/home/applications/fsl/5.0.10/lib:1:/home/applications/cuda/5.5/lib64:1:/home/applications/python/2.7.5/lib:1:/home/applications/cuda/5.5/lib:1
* LESSOPEN : ||/usr/bin/lesspipe.sh %s
* LOADEDMODULES : cuda/5.5:python/2.7.5:fsl/5.0.10:ANTs/1.9.4:freesurfer/dcnlab:matlab/2013b/front:mricron/6-2013:miniconda/2.7/4.2.12:afni/openmp:dcm2niix
* LOADEDMODULES_modshare : afni/openmp:1:miniconda/2.7/4.2.12:1:matlab/2013b/front:1:freesurfer/dcnlab:1:cuda/5.5:1:dcm2niix:1:mricron/6-2013:1:fsl/5.0.10:1:ANTs/1.9.4:1:python/2.7.5:1
* LOGNAME : pvier002
* LS_COLORS : rs=0:di=38;5;27:ln=38;5;51:mh=44;38;5;15:pi=40;38;5;11:so=38;5;13:do=38;5;5:bd=48;5;232;38;5;11:cd=48;5;232;38;5;3:or=48;5;232;38;5;9:mi=05;48;5;232;38;5;15:su=48;5;196;38;5;15:sg=48;5;11;38;5;16:ca=48;5;196;38;5;226:tw=48;5;10;38;5;16:ow=48;5;10;38;5;21:st=48;5;21;38;5;15:ex=38;5;34:*.tar=38;5;9:*.tgz=38;5;9:*.arc=38;5;9:*.arj=38;5;9:*.taz=38;5;9:*.lha=38;5;9:*.lz4=38;5;9:*.lzh=38;5;9:*.lzma=38;5;9:*.tlz=38;5;9:*.txz=38;5;9:*.tzo=38;5;9:*.t7z=38;5;9:*.zip=38;5;9:*.z=38;5;9:*.Z=38;5;9:*.dz=38;5;9:*.gz=38;5;9:*.lrz=38;5;9:*.lz=38;5;9:*.lzo=38;5;9:*.xz=38;5;9:*.bz2=38;5;9:*.bz=38;5;9:*.tbz=38;5;9:*.tbz2=38;5;9:*.tz=38;5;9:*.deb=38;5;9:*.rpm=38;5;9:*.jar=38;5;9:*.war=38;5;9:*.ear=38;5;9:*.sar=38;5;9:*.rar=38;5;9:*.alz=38;5;9:*.ace=38;5;9:*.zoo=38;5;9:*.cpio=38;5;9:*.7z=38;5;9:*.rz=38;5;9:*.cab=38;5;9:*.jpg=38;5;13:*.jpeg=38;5;13:*.gif=38;5;13:*.bmp=38;5;13:*.pbm=38;5;13:*.pgm=38;5;13:*.ppm=38;5;13:*.tga=38;5;13:*.xbm=38;5;13:*.xpm=38;5;13:*.tif=38;5;13:*.tiff=38;5;13:*.png=38;5;13:*.svg=38;5;13:*.svgz=38;5;13:*.mng=38;5;13:*.pcx=38;5;13:*.mov=38;5;13:*.mpg=38;5;13:*.mpeg=38;5;13:*.m2v=38;5;13:*.mkv=38;5;13:*.webm=38;5;13:*.ogm=38;5;13:*.mp4=38;5;13:*.m4v=38;5;13:*.mp4v=38;5;13:*.vob=38;5;13:*.qt=38;5;13:*.nuv=38;5;13:*.wmv=38;5;13:*.asf=38;5;13:*.rm=38;5;13:*.rmvb=38;5;13:*.flc=38;5;13:*.avi=38;5;13:*.fli=38;5;13:*.flv=38;5;13:*.gl=38;5;13:*.dl=38;5;13:*.xcf=38;5;13:*.xwd=38;5;13:*.yuv=38;5;13:*.cgm=38;5;13:*.emf=38;5;13:*.axv=38;5;13:*.anx=38;5;13:*.ogv=38;5;13:*.ogx=38;5;13:*.aac=38;5;45:*.au=38;5;45:*.flac=38;5;45:*.mid=38;5;45:*.midi=38;5;45:*.mka=38;5;45:*.mp3=38;5;45:*.mpc=38;5;45:*.ogg=38;5;45:*.ra=38;5;45:*.wav=38;5;45:*.axa=38;5;45:*.oga=38;5;45:*.spx=38;5;45:*.xspf=38;5;45:
* MAIL : /var/spool/mail/pvier002
* MANPATH : /home/applications/miniconda2.7/4.2.12/miniconda2/share/man:/home/applications/python/2.7.5/share/man:/home/applications/python/2.7.5/man:/home/share/Modules/4.1.3/share/man
* MANPATH_modshare : /home/applications/python/2.7.5/share/man:1:/home/applications/miniconda2.7/4.2.12/miniconda2/share/man:1:/home/share/Modules/4.1.3/share/man:1:/home/applications/python/2.7.5/man:1
* MATLABCMD : /home/applications/matlab/2013b/front/bin/matlab
* MNI_DIR : /home/applications/freesurfer_dcnlab/mni
* MODULEPATH : /home/share/Modules/4.1.3/modulefiles/linux-centos7-x86_64:/home/share/Modules/3.2.10/modulefiles
* MODULEPATH_modshare : /home/share/Modules/4.1.3/modulefiles/linux-centos7-x86_64:1:/home/share/Modules/3.2.10/modulefiles:1
* MODULESHOME : /home/share/Modules/4.1.3
* MODULES_CMD : /home/share/Modules/4.1.3/libexec/modulecmd.tcl
* MPLBACKEND : module://ipykernel.pylab.backend_inline
* OLDPWD : /home/pvier002
* PAGER : cat
* PATH : /home/data/nbc/nbclab-env/env-py3/bin:/home/applications/dcm2niix/build/bin:/home/applications/afni/abin:/home/applications/miniconda2.7/4.2.12/miniconda2/bin:/home/applications/mricron:/home/applications/spm12/canonical/:/home/applications/matlab/2013b/front/bin:/home/applications/freesurfer_dcnlab/bin:/home/applications/freesurfer_dcnlab/mni/bin:/home/applications/ANTs/1.9.4/bin:/home/applications/fsl/5.0.10/bin:/home/applications/fsl/5.0.10/etc:/home/applications/python/2.7.5/bin:/home/applications/cuda/5.5/bin:/opt/TurboVNC/bin:/home/share/Modules/4.1.3/bin:/usr/local/bin:/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/home/share/bin/:/bin/:/opt/ibutils/bin:/home/pvier002/bin:/home/share/bin/:/bin/:/home/applications/freesurfer_dcnlab/bin/freesurfer/
* PATH_modshare : /home/share/bin/:1:/usr/bin:1:/home/applications/cuda/5.5/bin:1:/home/applications/fsl/5.0.10/bin:1:/usr/local/bin:1:/home/applications/freesurfer_dcnlab/mni/bin:1:/home/applications/miniconda2.7/4.2.12/miniconda2/bin:1:/home/applications/matlab/2013b/front/bin:1:/opt/ibutils/bin:1:/home/share/Modules/4.1.3/bin:1:/bin/:1:/home/applications/mricron:1:/home/pvier002/bin:1:/home/applications/python/2.7.5/bin:1:/bin:1:/home/applications/freesurfer_dcnlab/bin:1:/home/applications/dcm2niix/build/bin:1:/home/applications/afni/abin:1:/home/applications/ANTs/1.9.4/bin:1:/opt/TurboVNC/bin:1:/usr/sbin:1:/home/applications/spm12/canonical/:1:/home/applications/fsl/5.0.10/etc:1:/usr/local/sbin:1
* PS1 : \[\e[1;37m\e[44m\][PY3]\[\e[0;0m\]\[\e[1;39m\]\u@\h:\W$\[\e[0m\] 
* PWD : /scratch/pvier002
* PYTHONPATH : /home/applications/python/2.7.5:/home/data/nbc/nbclab-env/
* SESSION_MANAGER : local/unix:@/tmp/.ICE-unix/4433,unix/unix:/tmp/.ICE-unix/4433
* SHELL : /bin/bash
* SHLVL : 4
* SLURMD_NODENAME : v001
* SLURM_CLUSTER_NAME : fiuhpcslurm
* SLURM_CONF : /home/share/slurm/19.05.3/etc/slurm.conf
* SLURM_CPUS_ON_NODE : 1
* SLURM_EXPORT_ENV : NONE
* SLURM_GET_USER_ENV : 1
* SLURM_GTIDS : 0
* SLURM_JOBID : 1698760
* SLURM_JOB_ACCOUNT : acc_nbc
* SLURM_JOB_CPUS_PER_NODE : 1
* SLURM_JOB_GID : 147
* SLURM_JOB_ID : 1698760
* SLURM_JOB_NAME : sys/dashboard/sys/bc_desktop/panther
* SLURM_JOB_NODELIST : v001
* SLURM_JOB_NUM_NODES : 1
* SLURM_JOB_PARTITION : visualization
* SLURM_JOB_QOS : normal
* SLURM_JOB_UID : 351143
* SLURM_JOB_USER : pvier002
* SLURM_LOCALID : 0
* SLURM_MEM_PER_CPU : 6436
* SLURM_NNODES : 1
* SLURM_NODEID : 0
* SLURM_NODELIST : v001
* SLURM_NODE_ALIASES : (null)
* SLURM_PRIO_PROCESS : 0
* SLURM_PROCID : 0
* SLURM_SUBMIT_DIR : /var/www/ood/apps/sys/dashboard
* SLURM_SUBMIT_HOST : hpcgui
* SLURM_TASKS_PER_NODE : 1
* SLURM_TASK_PID : 4315
* SLURM_TOPOLOGY_ADDR : v001
* SLURM_TOPOLOGY_ADDR_PATTERN : node
* SLURM_WORKING_CLUSTER : fiuhpcslurm:ms1:6817:8704:101
* SPM_PATH : /home/applications/spm12/
* SSH_ASKPASS : /usr/libexec/openssh/gnome-ssh-askpass
* SUBJECTS_DIR : /home/applications/freesurfer_dcnlab/subjects
* TERM : xterm-color
* TMPDIR : /scratch/afni
* USER : pvier002
* VTE_VERSION : 5202
* WEBSOCKIFY_CMD : /usr/bin/websockify
* XDG_DATA_DIRS : /home/pvier002/.local/share/flatpak/exports/share:/var/lib/flatpak/exports/share:/usr/local/share:/usr/share
* XDG_RUNTIME_DIR : /run/user/351143
* XDG_SESSION_ID : c34911
* _ : /home/data/nbc/nbclab-env/env-py3/bin/jupyter
* _LMFILES_ : /home/share/Modules/3.2.10/modulefiles/cuda/5.5:/home/share/Modules/3.2.10/modulefiles/python/2.7.5:/home/share/Modules/3.2.10/modulefiles/fsl/5.0.10:/home/share/Modules/3.2.10/modulefiles/ANTs/1.9.4:/home/share/Modules/3.2.10/modulefiles/freesurfer/dcnlab:/home/share/Modules/3.2.10/modulefiles/matlab/2013b/front:/home/share/Modules/3.2.10/modulefiles/mricron/6-2013:/home/share/Modules/3.2.10/modulefiles/miniconda/2.7/4.2.12:/home/share/Modules/3.2.10/modulefiles/afni/openmp:/home/share/Modules/3.2.10/modulefiles/dcm2niix
* _LMFILES__modshare : /home/share/Modules/3.2.10/modulefiles/dcm2niix:1:/home/share/Modules/3.2.10/modulefiles/mricron/6-2013:1:/home/share/Modules/3.2.10/modulefiles/fsl/5.0.10:1:/home/share/Modules/3.2.10/modulefiles/ANTs/1.9.4:1:/home/share/Modules/3.2.10/modulefiles/python/2.7.5:1:/home/share/Modules/3.2.10/modulefiles/afni/openmp:1:/home/share/Modules/3.2.10/modulefiles/miniconda/2.7/4.2.12:1:/home/share/Modules/3.2.10/modulefiles/matlab/2013b/front:1:/home/share/Modules/3.2.10/modulefiles/freesurfer/dcnlab:1:/home/share/Modules/3.2.10/modulefiles/cuda/5.5:1
* ahdir : /home/applications/afni/abin/help
* host : v001
* port : 5910
* project_name : [PY3]

