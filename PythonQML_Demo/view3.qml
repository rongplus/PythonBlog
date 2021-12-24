import QtQuick 2.0
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.12

import QtGraphicalEffects 1.0

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
                
      
		Item {
			 width: 300
			 height: 300

			 Rectangle {
			 id:aaa;
			 color:"yellow"
				 anchors.fill: parent
			 }

			 

			 DropShadow {
				 anchors.fill: aaa
				 horizontalOffset: 3
				 verticalOffset: 3
				 radius: 8.0
				 samples: 17
				 color: "#80000000"
				 source: aaa
			 }
		 }

		
		Item {
			 width: 300
			 height: 300

			 Rectangle {
			 color:"pink"
			 id:aaa1;
				 anchors.fill: parent
			 }

			 

			 DropShadow {
				 anchors.fill: aaa1
				 horizontalOffset: 3
				 verticalOffset: 3
				 radius: 8.0
				 samples: 17
				 color: "#80000000"
				 source: aaa1
			 }
		 }
	}
}