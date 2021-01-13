package de.moooon.acrylicons

import android.content.res.Resources
import android.os.Bundle
import android.widget.GridLayout
import android.widget.ImageView
import androidx.appcompat.app.AppCompatActivity
import java.lang.reflect.Field


class MainActivity : AppCompatActivity() {

    var drawables: Array<Field> = R.drawable::class.java.fields

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        setSupportActionBar(findViewById(R.id.toolbar))

        val layout = findViewById<GridLayout>(R.id.main_layout)

        var row = 0
        var column = 0

        for (drawable in drawables) {
            if (drawable.name.startsWith("acryl_")) {
                val imageView = ImageView(this)
                imageView.setImageResource(drawable.getInt(null))

                var layoutParams = GridLayout.LayoutParams(
                        GridLayout.spec(row, 1),
                        GridLayout.spec(column, 1))

                layoutParams.width = Resources.getSystem().displayMetrics.widthPixels / 2
                layoutParams.height = Resources.getSystem().displayMetrics.widthPixels / 2

                layout.addView(imageView, layoutParams)

                column += 1
                if (column == 2) {
                    column = 0
                    row += 1
                }
            }
        }
    }
}