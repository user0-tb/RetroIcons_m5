package de.moooon.acrylicons

import android.os.Bundle
import android.view.View
import android.widget.ImageView
import androidx.appcompat.app.AppCompatActivity
import java.lang.reflect.Field
import java.util.concurrent.ThreadLocalRandom


class MainActivity : AppCompatActivity() {

    var drawables: Array<Field> = R.drawable::class.java.fields
    var lastIcon: String = ""

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        setSupportActionBar(findViewById(R.id.toolbar))

        showRandomIcon(null)
    }

    override fun onResume() {
        super.onResume()

        showRandomIcon(null)
    }

    fun showRandomIcon(unused: View?) {
        var number = ThreadLocalRandom.current().nextInt(0, drawables.size)

        if (drawables[number].name.startsWith("acryl_")) {
            if (lastIcon == drawables[number].name) {
                showRandomIcon(null)
            } else {
                lastIcon = drawables[number].name
                findViewById<ImageView>(R.id.random_image).setImageDrawable(
                    resources.getDrawable(
                        drawables[number].getInt(null)
                    )
                )
            }
        } else {
            showRandomIcon(null)
        }
    }
}