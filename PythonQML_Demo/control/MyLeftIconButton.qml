import QtQuick 2.0

Rectangle {
    id: rec

    property alias img_src: icon.source
    property alias btn_txt: button.text
	property string img_active:""
	property string img_inactive:""

    property color clr_enter: "#dcdcdc"
    property color clr_exit: "#ffffff"
    property color clr_click: "#aba9b2"
    property color clr_release: "#ffffff"

    //Custom click signal
    signal clickedLeft()
    signal clickedRight()
    signal release()
	 color: clr_exit

    //width: 200
    //height: 60
	implicitWidth: rec.width
    implicitHeight: rec.height
	
    radius: 10

    Image {
        id: icon
        width: 20
        height: 20
        source: "qrc:/camera.png"
        fillMode: Image.PreserveAspectFit
        clip: true
        anchors.top: parent.top
        //anchors.right: parent.right
        anchors.left: parent.left
        anchors.margins: 10
    }
	

    Text {
        id: button
		color:"#416AB2"
		//width: 50
        //height: 50
        text: parent.parent.name

        anchors.left: icon.right
		anchors.right: parent.right
        anchors.topMargin: 1
        anchors.verticalCenter: icon.verticalCenter
        anchors.bottom: icon.bottom
        anchors.bottomMargin: 1

        font.bold: true
        font.pointSize: 9
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
            opacity: 1
        }

        //freed
        onReleased: {
            opacity: 0.8
            parent.release()
            console.log("Release")
        }

        //Pointer enter
        onEntered: {
            opacity: 1
			icon.source = img_active
			
//            console.log(button.text + " mouse entered")
        }

        //Pointer exit
        onExited: {
            opacity: 0.8
			icon.source = img_inactive
//            console.log(button.text + " mouse exited")
        }
    }
}

