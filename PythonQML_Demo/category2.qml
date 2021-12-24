import QtQuick 2.15
import QtQuick.Layouts 1.12
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.0
import QtQuick.Dialogs 1.2
import QtQuick.Controls 1.4

Rectangle
{
	id: main
	width: 968
    height: 900
	color:"gray"
	property int sp:15
	property string name: "Model Name"
	property string description: "Model detai"

	Button
	{
		id:btnBack
		y:10
		x:20
		anchors.left:space.left
		text:"back"
	}
	Text
	{
		y:20
	
		anchors.left: btnBack.right
		id: catalogueTitle
		text:"Category"
		
	}
	
	Rectangle {
		id: spaceFirst
		color: "blue"
		anchors.left:tlView.left
		anchors.right:trView.right
		height: 2
		anchors.top: catalogueTitle.bottom
		anchors.horizontalCenter: parent.horizontalCenter
	}

	
	Rectangle
	{
		id: tlView
		width: parent.width*0.35
		height: parent.height*0.6
		
        anchors.margins: main.sp
		anchors{
			top:spaceFirst.bottom
			left:parent.left
		}
		//color:"blue"
		Image {
			id: icon
			width: parent.width*0.8
			height: parent.height*0.8
			source: "Active.png"
			fillMode: Image.PreserveAspectFit
			clip: true
			anchors.top: parent.top
			//anchors.right: parent.right
			anchors.left: parent.left
			anchors.margins: 5
		}
	}
	
	Rectangle
	{
		id: trView
		height: parent.height*0.6
        anchors.margins: main.sp
		anchors{
			top:spaceFirst.bottom
			right:parent.right
			left:tlView.right
			//bottom:tlView.bottom
		}
		color:"white"
		Text {
			anchors.topMargin:10
			y:10
			id: title
			text: main.name
			anchors.left:space.left		
		}
		Rectangle {
			id: space
			//color: "blue"
			width: parent.width*0.9
			height: 2
			anchors.top: title.bottom
			anchors.horizontalCenter: parent.horizontalCenter
		}
		Text {
			y:10
			anchors.topMargin:10
			id: dateLabel
			text: main.name
			anchors.right:space.right		
		}

		Text {
			anchors.topMargin:10
			anchors.top: space.bottom
			anchors.left:space.left	
			text: main.description
		
		}
	}
	
	Rectangle
	{
		id: blView
		width: parent.width*0.35
		anchors.margins: main.sp
        //anchors.rightMargin: main.sp
		anchors{
			bottom:parent.bottom
			left:parent.left
			top:tlView.bottom
			//right:tlView.right

		}
		//color:"blue"
		Text {
			id:printerNameLabel
			width:parent.width*0.4
			x:10
			y:10
			anchors.topMargin:10
			text: "Printer"
			//anchors.left:parent.left		
		}
		Text {
			id:printerName
			text: "Printer"
			anchors.leftMargin:10
			anchors.topMargin:10
			y:10
			anchors.left:printerNameLabel.right		
		}

		Text {
			id:materialNameLabel
			width:parent.width*0.4
			text: "Printer"
			//anchors.left:parent.left	
			x:10
			anchors.topMargin:10
			anchors.top:printerNameLabel.bottom
		}
		Text {
			id:materialName
			text: "Printer"
			anchors.leftMargin:10
			anchors.topMargin:10
			anchors.left:materialNameLabel.right	
			anchors.top:printerName.bottom	
		}

		Text {
			id:reinforcedNameLabel
			width:parent.width*0.4
			text: "Reinforced"
			anchors.topMargin:10
			//anchors.left:parent.left	
			x:10
			anchors.top:materialName.bottom
		}
		Text {
			id:reinforcedName
			text: "None"
			anchors.leftMargin:10
			anchors.topMargin:10
			anchors.left:materialNameLabel.right	
			anchors.top:materialNameLabel.bottom	
		}

		Text {
			id:timeLabel
			width:parent.width*0.4
			text: "Time of Print"
			anchors.topMargin:10
			//anchors.left:parent.left	
			x:10
			anchors.top:reinforcedNameLabel.bottom
		}
		Text {
			id:timeName
			text: "55 minutes"
			anchors.leftMargin:10
			anchors.topMargin:10
			anchors.left:timeLabel.right	
			anchors.top:reinforcedName.bottom	
		}

		Text {
			id:additionalLabel
			width:parent.width*0.4
			anchors.topMargin:10
			text: "Additional Advice"
			//anchors.left:parent.left	
			x:10
			anchors.top:timeLabel.bottom
		}
		Text {
			id:additionalName
			text: "Other TPU"
			anchors.topMargin:10
			anchors.leftMargin:10
			anchors.left:timeLabel.right	
			anchors.top:timeName.bottom	
		}


	}
	
	Rectangle
	{
		id: brView

		anchors.margins: main.sp
		anchors{
			bottom:parent.bottom
			right:parent.right
			top:trView.bottom
			left: blView.right
		}
		color:"white"
		Button
		{
			id:btnCreate
			y:20
			x:20
			anchors.leftMargin:10
			width:btnContact.width
			text:"Create Print"
		}
		Text {
			y:20			
			anchors.left:btnContact.right	
			anchors.leftMargin:10
			text: "* Add this item to your print page"		
		}

		Button
		{
			id:btnContact
			anchors.top:btnCreate.bottom	
			x:20
			anchors.leftMargin:10
			anchors.topMargin:10
			text:"Contact Designer"
		}
		Text {
			anchors.bottom:btnContact.bottom			
			anchors.left:btnContact.right	
			anchors.leftMargin:10
			text: "* Contact the designer for additional support"		
		}

		Button
		{
			id:btnReport
			anchors.top:btnContact.bottom	
			x:20
			width:btnContact.width
			anchors.leftMargin:10
			anchors.topMargin:10
			text:"Report"
		}
		Text {
			anchors.bottom:btnReport.bottom			
			anchors.left:btnContact.right	
			anchors.leftMargin:10
			text: "* Report this product if you encounter any issue"		
		}


	}
}