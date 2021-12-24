import QtQuick 2.15
import QtQuick.Layouts 1.12
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.0



Rectangle {
    id: mainFrame
    visible: true
    width: 1440
    height: 850


    Rectangle {
        id: contentRect
		color: "yellow"
        property int currentTab: 0
       height:50
			width:parent.width
        //Menu
        Rectangle{
            id: menu
            height:50
			width:parent.width
            anchors{
                top: parent.top
                right: parent.right
                left: parent.left
            }
            color: ViciTheme.d3dWhite
            RowLayout {
                anchors.fill: parent
             
                spacing: 5
                clip: true
                Image {
                    id: logo
                    Layout.preferredHeight: parent.height * 0.8
                    Layout.preferredWidth: 100
                    fillMode: Image.PreserveAspectFit
                    source: "HomeIcon.png"
                    MouseArea {
                        anchors.fill: parent
                        onClicked: contentRect.currentTab = 0
                    }
                }

                Item {
                    Layout.preferredWidth: 120
                    Layout.fillHeight: true
                    Rectangle{
                        visible: contentRect.currentTab == 1
                        y: 5
                        anchors.top: btnAccount.bottom
                        height: 5
                        //radius: parent.height / 5
                        width: parent.width-10
                        color: "blue"
                    }

                    MyLeftIconButton {
						id: btn_camera36
						width:100
						height:40
						img_src: "HomeIcon.png";
						btn_txt: "camera"
						onClickedLeft: contentRect.currentTab = 1
						onClickedRight: setInfoText(btn_txt + " Right Button click")
					}
                }

                Item {
                    Layout.preferredWidth: 120
                    Layout.fillHeight: true
                    Rectangle{
                        visible: contentRect.currentTab == 2
                        y: 5
                        anchors.bottom: parent.bottom
                        height: 5
                        //radius: parent.height / 5
                        width: parent.width-10
                        color: "blue"
                    }

                    MyLeftIconButton {
						id: btn_camera3622
						width:100
						height:40
						img_src: "HomeIcon.png";
						btn_txt: "camera"
						onClickedLeft: contentRect.currentTab = 2
						onClickedRight: setInfoText(btn_txt + " Right Button click")
					}
                }
                 Item {
                    Layout.preferredWidth: 120
                    Layout.fillHeight: true
                    Rectangle{
                        visible: contentRect.currentTab == 3
                        y: 5
                        anchors.bottom: parent.bottom
                        height: 5
                        //radius: parent.height / 5
                        width: parent.width-10
                        color: "blue"
                    }

                    MyLeftIconButton {
						id: btn_camera3623
						width:100
						height:40
						img_src: "HomeIcon.png";
						btn_txt: "camera"
						onClickedLeft: contentRect.currentTab = 3
						onClickedRight: setInfoText(btn_txt + " Right Button click")
					}
                }
              
               IconCorner {
                    id: btnMessage
                    width:40
                    height:40
                    img_src: "HomeIcon.png";
                    btn_txt: "25"
                    onClickedLeft: setInfoText(btn_txt + " Left Button click")
                    onClickedRight: setInfoText(btn_txt + " Right Button click")
            
                }

               
                
            }

                



             
            }
        }

        StackLayout {
            id: contentStack
            currentIndex: contentRect.currentTab
            anchors {
                top: menu.bottom
                right: parent.right
                left: parent.left
                bottom: parent.bottom
            }

            Rectangle {
                id: addFile34
                anchors.fill: parent
                 height: 750
                 width: parent.width
                 implicitHeight: 622
    implicitWidth:  1200
                color: "blue"
            }

            Rectangle {
                id: addFile
                anchors.fill: parent
                 height: 750
                 width: parent.width
                 implicitHeight: 622
    implicitWidth:  1200
                color: "red"
            }

            Rectangle {
                id: addFile333
                anchors.fill: parent
                 height: 750
                 width: parent.width
                 implicitHeight: 600
    implicitWidth:  1200
                color: "green"
            }
        }

        DropShadow {
            anchors.fill:  menu
            verticalOffset: 5
            radius: 8
            samples: 17
            color: ViciTheme.shadowColor
            source: menu
        }

    
  
}
