import QtQuick 2.15
import QtQuick.Layouts 1.12
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.0
import QtQuick.Dialogs 1.2

Rectangle
{
	id: main
	width: 800
    height: 900
	color:"gray"
	
	Text
	{
		y:20
		x:40
		id: title
		text:"Category"
		
	}
	
	Rectangle {
		id: space
		color: "red"
		width: parent.width*0.9
		height: 2
		anchors.top: title.bottom
		//anchors.horizontalCenter: parent.horizontalCenter
	}
		
	Rectangle {
		id: catalogueFrame
		color: "white"
		anchors.top: space.bottom
		anchors.verticalCenter: parent.verticalCenter	   
		width: parent.white*0.9
		height: parent.height*0.9
		property int currentTab: 0
	
		
			

			
	}
}
