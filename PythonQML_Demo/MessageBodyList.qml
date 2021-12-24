import QtQuick 2.9
import QtQuick.Window 2.2
import QtQuick.Controls 1.4
import QtQuick.Controls.Styles 1.4
Rectangle {
    visible: true
    width: parent.width
    height: parent.height
    color:"gray"
    
 
    ListView {
        id: listView
        clip: true
        anchors.fill: parent
        spacing :0
 
        highlight: Rectangle {
            width: listView.width*0.9
            height: 40
            color: "lightsteelblue"
            radius: 15
            anchors.leftMargin: 20

            anchors.rightMargin: 20
 
            Behavior on y {
                SpringAnimation {
                    spring: 3
                    damping: 0.2
                }
            }
        }
        highlightFollowsCurrentItem: true
        focus: true
        delegate: Rectangle {
            width: listView.width*0.9
            height: 200 
            radius: 5 
            
           
            anchors.bottomMargin:10
            color: "#DBDBDB"

            Rectangle
            {
                width: parent.width
                height: 180 
                radius: 5 
                border.width:1
                border.color:"black"
                anchors.bottomMargin:10
                anchors.rightMargin:10
                color: "white"
                 Text {
                                y:20
                                x:10
                                text: "Message\nhello"
                            
                            }
            }
            //color: listView.currentIndex == index ? "gray":tempcolor
           
            MouseArea{
                anchors.fill: parent
                hoverEnabled: true
                onClicked: {
                    listView.currentIndex = index
                    //console.log(index)
                }
                onEntered: {
                    tempcolor = "#a7e094"
                }
 
                onExited: {
                    tempcolor = "transparent"
                }
            }
        }
        model: ListModel {
            ListElement {
                name: "Grey"
                colorCode: "grey"
            }
 
            ListElement {
                name: "Red"
                colorCode: "red"
            }
 
            ListElement {
                name: "Blue"
                colorCode: "blue"
            }
 
            ListElement {
                name: "Green"
                colorCode: "green"
            }
            ListElement {
                name: "Grey"
                colorCode: "grey"
            }
 
            ListElement {
                name: "Red"
                colorCode: "red"
            }
 
            ListElement {
                name: "Blue"
                colorCode: "blue"
            }
 
            ListElement {
                name: "Green"
                colorCode: "green"
            }
            ListElement {
                name: "Grey"
                colorCode: "grey"
            }
 
            ListElement {
                name: "Red"
                colorCode: "red"
            }
 
            ListElement {
                name: "Blue"
                colorCode: "blue"
            }
 
            ListElement {
                name: "Green"
                colorCode: "green"
            }
            ListElement {
                name: "Grey"
                colorCode: "grey"
            }
 
            ListElement {
                name: "Red"
                colorCode: "red"
            }
 
            ListElement {
                name: "Blue"
                colorCode: "blue"
            }
 
            ListElement {
                name: "Green"
                colorCode: "green"
            }
        }
    }
}