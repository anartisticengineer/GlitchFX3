<h1>Glitch FX 3</h1>
<h2>The third installment of the glitch fx generator!</h2>
<section>
    <h3>Setup</h3>
    <div>
        This project is intended for use with Python 3 and assumes some prior knowledge.
    </div>
</section>
<section>
    <h3>Packages</h3>
    <div>The following packages should be installed in order to run the generator <strong>(these can also be found in the requirements.txt file)</strong></div>
    <ul>
        <li>opencv-python</li>
        <li>numpy</li>
        <li>perlin_noise</li>
        <li>pytest (for unit testing)</li>
    </ul>
</section>
<section>
    <h3>Instructions</h3>
    <ol>
        <li>Upon running the main script, a dialog box should pop up to select an image (so far, only jpg and png is supported)</li>
        <li>When an image is selected, the python prompt should show up in the console: <code>Enter an effect (or x to exit):</code></li>
        <li>Enter an effect by sending an input of the form: <code>effect_name/p_key p_value/p_key p_value...</code> <i>(More detail on the types of available effects can be found below)</i></li>
        <li>When finished, press the x key to exit view the final image. The image should pop up in a new window.</li>
        <li>If you wish to save the image, press the s key, and the dialog box will open for you to save the image.
            Press any other key otherwise if you don't want to save it. Either option will exit the program.
        </li>
    </ol>
</section>
<section>
    <h3>Effects Reference</h3>
    <div>When applying a new effect, the console input should be of the form: 
        <code>effect_name/p_key p_value/p_key p_value...</code> 
        where <code>p_key p_value</code> can be repeated for as many parameters available, or omitted altogether (will use the default values in that case)
    </div>
    <h4>Available parameters</h4>
    <table>
        <thead>
            <td>Effect name</td>
            <td>Available parameters (p_key)</td>
        </thead>
        <tbody>
            <tr>
                <td>noisy</td>
                <td>p</td>
            </tr>
            <tr>
                <td>scanlines</td>
                <td>or</td>
            </tr>
            <tr>
                <td>highpass</td>
                <td>p, k, a</td>
            </tr>
            <tr>
                <td>warp</td>
                <td>type, f</td>
            </tr>
            <tr>
                <td>wavy</td>
                <td>oct</td>
            </tr>
        </tbody>
    </table>
    <h4>Expected values</h4>
    <table>
        <thead>
            <td>p_key</td>
            <td>Meaning</td>
            <td>Expected value (p_value)</td>
        </thead>
        <tbody>
            <tr>
                <td>p</td>
                <td>Percent</td>
                <td>float: 0.0 - 1.0</td>
            </tr>
            <tr>
                <td>or</td>
                <td>Orientation</td>
                <td>str: 'h' or 'v'</td>
            </tr>
            <tr>
                <td>k</td>
                <td>Kernel Size</td>
                <td>int: odd number (k%2 = 1)</td>
            </tr>
            <tr>
                <td>a</td>
                <td>Amplitude</td>
                <td>float: > 0.0</td>
            </tr>
            <tr>
                <td>type</td>
                <td>Warp type</td>
                <td>str: {'rotateX', 'rotateY', 'shearX' or 'shearY'}</td>
            </tr>
            <tr>
                <td>f</td>
                <td>Factor</td>
                <td>int or float (experiment a bit with this one)</td>
            </tr>
            <tr>
                <td>oct</td>
                <td>Octaves</td>
                <td>int: >= 1</td>
            </tr>
        </tbody>
    </table>
    <h4>Examples</h4>
    <div>The following are examples you can try with the prompt in order to apply effects:</div>
    <ul>
        <li><code>noisy</code> will apply the noisy filter with the default values (percent of 0.1 in this case)</li>
        <li><code>noisy/p 0.7</code> will apply the noisy filter with a percent value of 0.7</li>
        <li><code>scanlines/or v</code> will apply the scanlines filter with a vertical (v) orientation</li>
        <li><code>warp/type shearY/f 5</code> will apply the warp filter with a type of shear Y and a factor of 5</li>
    </ul>
</section>
