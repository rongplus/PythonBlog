import QtQuick 2.0
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.12



Rectangle {
    width: 1000
    height: 200
    color: "gray"
	property string name:"hello"
	function setInfoText(str)
    {
        print(str)
    }

	RowLayout {
                anchors.fill: parent
              
                spacing: 5
                clip: true
                Image {
                    id: logo
                    Layout.preferredHeight: parent.height * 0.8
                    Layout.preferredWidth: 150
                    fillMode: Image.PreserveAspectFit
                    source: "HomeIcon.png"
                    MouseArea {
                        anchors.fill: parent
                        onClicked: {}
                    }
                }
      ToolButton {
                    id: control
                     width: 300
                //height: 100
                  //  icon.source: menuItemIcon
                    text: qsTr("tr1")
                    font.family: "Helvetica"
                    font.bold: true
                    antialiasing: true

                    contentItem: Item {
                        Row {
                            //anchors.horizontalCenter: parent.horizontalCenter
                            spacing: 5
                            Image {
                                source: "HomeIcon.png"
                                width: control.icon.width
                                height: control.icon.height
                                anchors.verticalCenter: parent.verticalCenter
                            }
                            Text {
                                text: "Test"
                                font: control.font
                                anchors.verticalCenter: parent.verticalCenter
                            }
                        }
                    }
                }
				
		 MyIconButton {
            id: btn_camera
            img_src: "HomeIcon.png";
            btn_txt: "camera"
            onClickedLeft: setInfoText(btn_txt + " Left Button click")
            onClickedRight: setInfoText(btn_txt + " Right Button click")
        }
		MyLeftIconButton {
            id: btn_camera36
			width:100
			height:40
            img_src: "HomeIcon.png";
			img_active:"Active.png"
			img_inactive:"HomeIcon.png"
            btn_txt: "show name"
            onClickedLeft: setInfoText(btn_txt + " Left Button click")
            onClickedRight: setInfoText(btn_txt + " Right Button click")
        }
		IconButton123
		{
		id: messageButton
                    //anchors.centerIn: parent
                    width: 150
                    text: "Message"
                    textColor: "black"
                    iconSource: "HomeIcon.png"
		}
		
		IconCorner
		{
		
			width:40
			height:40
            img_src: "Account2.png";
			img_active:"Account1.png"
            img_inactive:"Account2.png"
			
            btn_txt: "99+"
            onClickedLeft: setInfoText(btn_txt + " Left Button click")
            onClickedRight: setInfoText(btn_txt + " Right Button click")
		}
		IconCorner
		{
		
			width:40
			height:40
            img_src: "Account2.png";
			img_active:"Account1.png"
            img_inactive:"Account2.png"
			
            btn_txt: "9"
            onClickedLeft: setInfoText(btn_txt + " Left Button click")
            onClickedRight: setInfoText(btn_txt + " Right Button click")
		}
		IconCorner
		{
		
			width:40
			height:40
            img_src: "Account2.png";
			img_active:"Account1.png"
            img_inactive:"Account2.png"
			
            //btn_txt: ""
            onClickedLeft: setInfoText(btn_txt + " Left Button click")
            onClickedRight: setInfoText(btn_txt + " Right Button click")
		}
	}
}