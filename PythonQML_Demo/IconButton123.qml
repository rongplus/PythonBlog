import QtQuick 2.15
import QtQuick.Controls 2.15 as C



C.Button {
    property color textColor: black
    property color hoverColor: gray
    property string iconSource: ""
    property int iconSize: 20

    antialiasing: true
    id: control
    flat: true
    implicitWidth: 100
    implicitHeight: 40
    icon.width: control.width * 0.8
    icon.height: control.width * 0.8

    contentItem: Text {
        id: buttonText
        text: control.text
        color: control.textColor
        font: ViciTheme.helveticaBold
        //anchors.centerIn: parent
        anchors.left: buttonImage.right
		anchors.right: parent.right
        anchors.bottom: icon.bottom
        anchors.bottomMargin: 5
        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignVCenter
    }


    background: Rectangle{
        color: control.hovered ? control.hoverColor : "transparent"
    }

    Image {
        id: buttonImage
        anchors.top: parent.top   
        anchors.left: parent.left
        //anchors.right: parent.right
        anchors.margins: 10
        height: control.iconSize
        width: control.iconSize
        source: control.iconSource
        mipmap: true
    }
}
