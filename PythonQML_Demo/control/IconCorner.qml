import QtQuick 2.0

Rectangle {
    id: rec
	color:"transparent"
    property alias img_src: icon.source
    property alias btn_txt: button.text

    //Custom click signal
    signal clickedLeft()
    signal clickedRight()
    signal release()

    //width: 200
    //height: 60
	implicitWidth: rec.width
    implicitHeight: rec.height
	
    radius: 10

    Image {
        id: icon
        width: 30
        height: 30
        source: "qrc:/camera.png"
        fillMode: Image.PreserveAspectFit
        clip: true
        anchors.top: parent.top
        //anchors.right: parent.right
        anchors.left: parent.left
        anchors.margins: 5
    }

    Rectangle {
        id: backRect
        color: ViciTheme.alertRed
        anchors.right: parent.right
        anchors.topMargin: 1
        y:-10
        anchors.bottomMargin: 10
        width: 25
        height: 25
        radius: 12
    }
			

    Text {
        id: button		
        text: qsTr("button")
        anchors.verticalCenter: backRect.verticalCenter
		anchors.horizontalCenter: backRect.horizontalCenter
        font.bold: true
        font.pointSize: 7
		color:ViciTheme.d3dWhite
    }

    MouseArea {
        id: mouseArea
        anchors.fill: parent
        hoverEnabled: true

        //Accept left and right keys input
        acceptedButtons: Qt.LeftButton | Qt.RightButton
        onClicked: {
            //Left click
            if (mouse.button === Qt.LeftButton)
            {
                parent.clickedLeft()
//                console.log(button.text + " Left button click")
            }
            else if(mouse.button === Qt.RightButton)
            {
                parent.clickedRight()
//                console.log(button.text + " Right button click")
            }
        }

        //Press
        onPressed: {
            color = clr_click
        }

        //freed
        onReleased: {
            color = clr_enter
            parent.release()
            console.log("Release")
        }

        //Pointer enter
        onEntered: {
            color = clr_enter
            console.log(button.text + " mouse entered")
        }

        //Pointer exit
        onExited: {
            color = clr_exit
//            console.log(button.text + " mouse exited")
        }
    }
}

