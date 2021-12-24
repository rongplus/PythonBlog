import QtQuick 2.0

Rectangle {
    id: rec

    property alias img_src: icon.source
   

    property color clr_enter: "#dcdcdc"
    property color clr_exit: "#ffffff"
    property color clr_click: "#aba9b2"
    property color clr_release: "#ffffff"

    //Custom click signal
    signal clickedLeft()
    signal clickedRight()
    signal release()

    width: 50
    height: 50
    radius: 10

    Image {
        id: icon
        width: 40
        height: 40
        source: "qrc:/camera.png"
        fillMode: Image.PreserveAspectFit
        clip: true
        anchors.top: parent.top
        anchors.right: parent.right
        anchors.left: parent.left
        anchors.margins: 10
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
//            console.log(button.text + " mouse entered")
        }

        //Pointer exit
        onExited: {
            color = clr_exit
//            console.log(button.text + " mouse exited")
        }
    }
}

