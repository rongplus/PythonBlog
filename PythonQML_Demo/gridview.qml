import QtQuick 2.5
import QtQuick.Window 2.2
import QtQuick.Layouts 1.1
import QtQuick.Controls 1.4

Window {
    width: 600; height: 400; visible: true

    GridLayout {
        id: grid
        anchors.fill: parent
        columns: 2
        rowSpacing: 5
        columnSpacing: 5
        anchors.margins: 5
        // example models
        property var titles: [ "title1", "title2", "title3", "title4", "title5" ]
        property var values: [ "value1", "value2", "value3", "value4", "value5" ]

        Repeater {
            model: grid.titles
            Label {
                Layout.row: index
                Layout.column: 0
                Layout.fillWidth: true
                Layout.fillHeight: true
                text: modelData
            }
        }

        Repeater {
            model: grid.values
            TextArea {
                Layout.row: index
                Layout.column: 1
                Layout.fillWidth: true
                Layout.fillHeight: true
                text: modelData
            }
        }
    }
}