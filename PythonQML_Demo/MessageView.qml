import QtQuick 2.15
import QtQuick.Layouts 1.12
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.0
import QtQuick.Dialogs 1.2
import QtQuick.Controls 1.4
import QtQuick.Controls.Styles 1.4

Rectangle
{
	id: main
	width: 1240
    height: 900
	color:"gray"
    property int currentTab: 0



     RowLayout 
    {
        anchors.fill: parent
        Rectangle
        {
            id:messageListRect
            Layout.preferredHeight: parent.height
            Layout.preferredWidth: parent.width*0.3
            anchors.left:parent.left
            anchors.top: parent.top
            color:"gray"

            Rectangle{
                id:topRect
                anchors.topMargin:20
                width:parent.width
                height:parent.height
                y:20
                color:"gray"
                 RowLayout 
                {
                    id:toolBar
                    width:parent.width
                    height:50
                    Rectangle{
                        width:100
                        Text {
                        width:150
                        text: "Message"
                        color:"white"
                        font.pointSize:  19 
                        x:10
                        anchors.verticalCenter: parent.verticalCenter
                    
                    }
                    }
                    
                    MyIconButton {
                        id: buttonImage1                       
                    
                        height: 40
                        width: 40
                        img_src: "Active.png"
                        onClickedLeft:main.currentTab=1
                      
                    }
                    MyIconButton {
                        id: buttonImage2                       
                    
                        height: 40
                        width: 40
                        img_src: "Active.png"
                        onClickedLeft:main.currentTab=0
                      
                    }
                    Button {
              x:10
              text: "Refresh Orders"
              style: ButtonStyle {
                    background: Rectangle {
                        implicitWidth: 100
                        implicitHeight: 25
                        border.width: control.activeFocus ? 2 : 1
                        border.color: "#888"
                        radius: 4
                       
                    }
                }
                onClicked:console.log("ccccccccc")
             
          }
                    MyIconButton {
                        id: buttonImage4                       
                    
                        height: 40
                        width: 40
                        img_src: "Active.png"
                      
                    }
                }

                TextField {		
                    id: searchText
                    anchors.top:	toolBar.bottom	
                    anchors.leftMargin:10
                    anchors.rightMargin:10
                    anchors.topMargin:10
                    anchors.left:parent.left
                    anchors.horizontalCenter: parent.horizontalCenter                    
                    height:40

				} 

                MessageList {
                    id: listView
                    anchors.top:searchText.bottom
                    anchors.bottom:parent.bottom
                    anchors.left:parent.left
                    //anchors.right:parent.right
                    width:parent.width
                    anchors.topMargin:10
                    Layout.fillWidth: true
                    Layout.fillHeight: true                   
                
                }



            }

           
        }

        Rectangle {
            width: parent.width*70
            height: parent.height
            anchors.left:messageListRect.right

            StackLayout {
                id: contentStack
                currentIndex: main.currentTab
                anchors.fill:parent

                MessageBody{
                    width: parent.width
                    height: parent.height
                }

                ComposeMessage
                {
                    width: parent.width
                    height: parent.height
                  
                }
             }

           
        }//end right
    }


}