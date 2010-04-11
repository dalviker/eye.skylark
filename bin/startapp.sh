#!/bin/sh
#
JAVA_OPTS="-Xmx512m -ea $JAVA_OPTS"
#JPDA_OPTS="-Xdebug -Xrunjdwp:transport=dt_socket,address=8000,server=y,suspend=n"


SKYLARK_HOME=`pwd`/..
SKYLARK_VERSION=`cat $SKYLARK_HOME/VERSION.txt`
SKYLARK_LIB=$SKYLARK_HOME/lib
SKYLARK_BAIBOX=$SKYLARK_HOME/skylark-baibox.jar
SKYLARK_APP=$1
JAVA=$JAVA_HOME/bin/java
echo "JAVA_HOME=$JAVA_HOME"
echo "SKYLARK_HOME=$SKYLARK_HOME"
echo "SKYLARK_VERSION=$SKYLARK_VERSION"
echo "SKYLARK_LIB=$SKYLARK_LIB"
echo "SKYLARK_APP=$SKYLARK_APP"
$JAVA -fullversion

INSTANCE=$SKYLARK_HOME/tmp/$instance
rm -fr $INSTANCE
mkdir -p $INSTANCE/logs

properties=""
echo "properties=$properties"

classpath=`find $SKYLARK_LIB -name "*.jar" | tr '\n' ':'`$SKYLARK_BAIBOX
#echo "classpath=$classpath"

if [ -z "$SKYLARK_APP" ]
then
    echo "Please set SKYLARK_APP path , like : '/media/study/workspace/skylark/deploy/targetdir/guestbook/war' "
    exit 1
else
    echo "start app : $SKYLARK_APP"
    $JAVA $properties -cp $classpath $JAVA_OPTS  org.skylark.AppServerMain "$SKYLARK_APP"
fi
