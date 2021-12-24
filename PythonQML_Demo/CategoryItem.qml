//IconButton.qml
import QtQuick 2.6
import QtQuick.Controls 2.0
import QtQuick.Controls.Material 2.0
import QtQuick.Layouts 1.12

Rectangle {
    id: item   
	property alias label: itemLabel.text
	property alias img: itemImg.source
	color: "transparent"
	width:150
	height:180
    ColumnLayout{
     spacing: 2
     Rectangle {
          Layout.alignment: Qt.AlignCenter
		  
         //color: "transparent"
		 width:150
		 height:100
		 //color: 'gray'
		 Image {
		 id:itemImg
			 anchors.fill: parent
			 anchors.topMargin:20
			 Layout.alignment: Qt.AlignCenter
			 fillMode: Image.PreserveAspectFit
			 source: "Active.png"
		 }
        
     }
	 Rectangle {
         Layout.alignment: Qt.AlignCenter
         color: "white"
		 width:150
		 height:20
     }
	 
	 Rectangle {
         Layout.alignment: Qt.AlignCenter
         color: "red"
		 width:150
		 height:20
		 Text {
			id:itemLabel
			width:150
			elide :Text.ElideRight
			//wrapMode: "WordWrap"
			//Layout.alignment: Qt.AlignHCenter		
			//anchors.horizontalCenter: parent.horizontalCenter
			Layout.alignment: Qt.AlignCenter
			//text: "Hello <p style=color: #0444a0><b>fddf"  + "</b></p>"
			TextMetrics {
    id: textMetrics
    font: itemLabel.font
    text: itemLabel.text
    elide: itemLabel.elide
  }
		}
		 
        
     }
	 
	  
	 
	 
	 
 }
 MouseArea {
        anchors.fill: parent
        onClicked: console.log("log, click item")
    }

}