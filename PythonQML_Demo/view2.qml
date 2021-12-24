import QtQuick 2.0
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.12
import QtGraphicalEffects 1.0
Rectangle {
    id: mainFrame
    //implicitHeight: 500
    //implicitWidth:  1200
	width: 600
    height: 200
    color:"gray"
    RowLayout {
     id: layout
     anchors.fill: parent
     spacing: 6
     Rectangle {
         color: 'teal'
         Layout.fillWidth: true
         Layout.minimumWidth: 50
     
		  width: parent.width*0.3
		  height:parent.height
        
         Text {
             anchors.centerIn: parent
             text: parent.width + 'x' + parent.height
         }
     }
     Rectangle {
         color: 'plum'
         Layout.fillWidth: true
         Layout.minimumWidth: 100
         width: parent.width*0.6
		 height:parent.height
          Image {
        id: img
        source: 'woman.png'
        width: 500
        height: 500
        fillMode: Image.PreserveAspectCrop
        layer.enabled: true
        layer.effect: OpacityMask {
            maskSource: mask
        }
    }

 
     }
 }

}