import QtQuick 2.9
import QtQuick.Window 2.2
import QtQuick.Controls 1.4
import QtQuick.Controls.Styles 1.4
Rectangle {
    visible: true
    width: 640
    height: 900
    
 
    ListView {
        id: listView
        clip: true
        anchors.fill: parent
        spacing :0
 
        highlight: Rectangle {
            width: listView.width
            height: 40
            color: "lightsteelblue"
            radius: 5
 
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
            width: listView.width
            height: 40
 
            radius: 5
 
            border.width:1
            property color tempcolor: "transparent"
            color: tempcolor
            Row {
                id: row1
                anchors.fill: parent
                spacing: 10
                anchors.leftMargin: 10
 
                Text {
                    text: index+1
                    anchors.verticalCenter: parent.verticalCenter
                    font.bold: true
                    font.pointSize: listView.currentIndex == index ? 19 : 13
                }
 
                Rectangle {
                    width: 30
                    height: 30
                    color: colorCode
                    anchors.verticalCenter: parent.verticalCenter
 
                }
 
                Text {
                    text: name
                    anchors.verticalCenter: parent.verticalCenter
                    font.bold: true
                    font.pointSize: listView.currentIndex == index ? 19 : 13
                }
 
            }
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