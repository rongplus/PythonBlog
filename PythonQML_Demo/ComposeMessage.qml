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
	anchors.fill:parent
	color:"white"
  

    Rectangle
    {
        x:10
        y:10
        radius:10
        width:parent.width*0.8
        height:parent.height*0.8
        anchors.rightMargin:10
      
        color:"#DBDBDB"

        TextField {		
            id: receiverName
            y:10
            anchors.leftMargin:20
            anchors.rightMargin:10
            anchors.topMargin:10
            anchors.left:parent.left
            anchors.horizontalCenter: parent.horizontalCenter                    
            height:40
        } 

        TextField {		
            id: messageTitle
            anchors.top:receiverName.bottom	
            anchors.leftMargin:20
            anchors.rightMargin:10
            anchors.topMargin:10
            anchors.left:parent.left
            anchors.horizontalCenter: parent.horizontalCenter                    
            height:40
        } 
        Rectangle
		{
            id: messageContent
            anchors.top:messageTitle.bottom	
            anchors.topMargin:10
			
			 width: parent.width; 
             height: 120 
			 color:"#DBDBDB"
			
			TextArea {
				id:messageInput
				height: 120 
				width: parent.width*0.9
				x:20
				//anchors.horizontalCenter: parent.horizontalCenter
				focus: true
				text: ""
			}
		}

        Button{
            id:btnDiscard
            anchors.top:messageContent.bottom	
            text:"Discard"
            x:200
        }
        Button{
            anchors.top:messageContent.bottom	
            anchors.left:btnDiscard.right	
            text:"Send"
            
        }
    }
}