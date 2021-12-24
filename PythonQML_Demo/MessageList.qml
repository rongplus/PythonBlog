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
 
        
        focus: true
        delegate: Rectangle {
            width: listView.width
            height: 80
 
            radius: 5


            Rectangle {
                visible:listView.currentIndex == index
                width: listView.width
                height: 80
                color: "#99416AB2"
                radius: 15           
    
            }//heigh
 
            //border.width:1
            property color tempcolor: "gray"
            color: listView.currentIndex == index ? "gray":tempcolor
            Row {
                id: row1
                anchors.fill: parent
                //spacing: 10
                //anchors.leftMargin: 10
 
                Rectangle
                {
                    id: headRect
                    color:"transparent"
                    //color: listView.currentIndex == index ? "lightsteelblue":"gray"
                    width:50
                    
                    height:parent.height
                    CircleLetter {
                    x:5
                    color: colorCode
                    //color: colorCode
                    text:name[0]
                    anchors.verticalCenter: parent.verticalCenter
                    }

                }
                
 
                Rectangle {
                   
                    height: parent.height
                    anchors.left:headRect.right
                    anchors.right:parent.right
                    //anchors.leftMargin:10
                    color:"transparent"
                    //color: listView.currentIndex == index ?"lightsteelblue":"gray"
                    anchors.verticalCenter: parent.verticalCenter
                    //anchors.rightMargin:10
                    
                    Text {
                        id: mailTitle
                        x:10
                        text: "<b>Receiver</b><br>Hello Michal<br>title"
                        //anchors.verticalCenter: parent.verticalCenter
                    
                        y:20
                        anchors.topMargin:10
                        anchors.leftMargin:10
                        //font.bold: true
                        color:"white"
                        //font.pointSize: listView.currentIndex == index ? 19 : 13
                    }
                    Text {
                        id: mailTime
                        text: name
                        //anchors.verticalCenter: parent.verticalCenter
                
                        anchors.right: parent.right
                        anchors.bottom:parent.bottom
                        anchors.topMargin:10
                        anchors.leftMargin:10
                        anchors.rightMargin:10
                        //font.bold: true
                        color:"white"
                        horizontalAlignment: Text.AlignRight
                        //font.pointSize: listView.currentIndex == index ? 19 : 13
                    }
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