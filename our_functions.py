

def event_reconstruction(event_id, event_meta_df, sensor_data_df, sensor_geometry_df, auxiliary=False):
    
    event_meta = event_meta_df.loc[event_meta_df['event_id'] == event_id]
    azimuth = event_meta['azimuth'].values[0]
    zenith = event_meta['zenith'].values[0]
    print('azimuth: '+str(azimuth))

    # Filter sensor data for the given event_id
    event_sensors = sensor_data_df[sensor_data_df.index == event_id]
    
    x_all = sensor_geometry_df['x'].values
    y_all = sensor_geometry_df['y'].values
    z_all = sensor_geometry_df['z'].values

    # Get event sensor coordinates based on auxiliary option
    if auxiliary:

        auxiliary_sensor_ids = event_sensors[event_sensors['auxiliary'] == True]
        auxiliary_sensor_ids = auxiliary_sensor_ids.drop_duplicates(subset=['sensor_id'])    
        event_sensor_coordinates = sensor_geometry[sensor_geometry.index.isin(auxiliary_sensor_ids['sensor_id'])]
        charges = auxiliary_sensor_ids['charge'].values
        times = auxiliary_sensor_ids['time'].values


    else:
        event_sensors = event_sensors.drop_duplicates(subset=['sensor_id'])
        event_sensor_coordinates = sensor_geometry_df[sensor_geometry_df.index.isin(event_sensors['sensor_id'])]
        charges = event_sensors['charge'].values
        times = event_sensors['time'].values
        print('len charges: '+str(charges.shape))

    charge_min = np.min(charges)
    charge_max = np.max(charges)
    marker_sizes = 5 + (200 * ((charges - charge_min) / (charge_max - charge_min)) ) # Adjust the range of marker sizes as needed

    time_min = np.min(times)
    plottimes = (times - time_min)/1000. # Adjust the range of marker sizes as needed


    print(event_sensor_coordinates['x'].shape, event_sensor_coordinates['y'].shape, event_sensor_coordinates['z'].shape,marker_sizes.shape)
    # Create a 3D plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x_all, y_all, z_all, c='gray', marker='o', s = 1, alpha = .1)

    # Plot the triggered sensors with markers

    colormap = plt.cm.plasma
    plot = ax.scatter(event_sensor_coordinates['x'].values, event_sensor_coordinates['y'].values, event_sensor_coordinates['z'].values, marker='o', s=marker_sizes, c=plottimes, cmap=colormap)


    center_x = np.mean(event_sensor_coordinates['x'].values)
    center_y = np.mean(event_sensor_coordinates['y'].values)
    center_z = np.mean(event_sensor_coordinates['z'].values)

    direction = np.array([
        np.sin(zenith) * np.cos(azimuth),
        np.sin(zenith) * np.sin(azimuth),
        np.cos(zenith)
    ])

    center = np.array([center_x,center_y,center_z])
    arrow_length = 1600
    arrow_center = center - (arrow_length / 2) * direction
    arrow_end = center + (arrow_length / 2) * direction

    # Plot the arrow passing through the center point
    ax.quiver(arrow_center[0], arrow_center[1], arrow_center[2],
            direction[0], direction[1], direction[2], color='red',
            length=arrow_length,arrow_length_ratio=.1)


    cax = fig.add_axes([0.25, 0.87, 0.53, 0.03])  # Adjust the position and size as needed
    cbar = fig.colorbar(plot, cax=cax, orientation='horizontal')
    cax.text(5.5, 1.75, r'Time [$ \mu $s]', ha='center', va='center')

    # cbar = fig.colorbar(plot, ax=ax,shrink=.7)

    # Set labels and title
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_xlim(-600,600)
    ax.set_ylim(-600,600)
    ax.set_zlim(-600,600)
    ax.set_title(f'Neutrino Event {event_id}, Aux = {auxiliary}',loc="center", y=1.18)
    ax.grid(False)

    # fig.show()
    # Show the plot
    plt.show()


def event_reconstruction_gif(event_id, event_meta_df, sensor_data_df, sensor_geometry_df, auxiliary=False):
       
    event_meta = event_meta_df.loc[event_meta_df['event_id'] == event_id]
    azimuth = event_meta['azimuth'].values[0]
    zenith = event_meta['zenith'].values[0]
    print('azimuth: '+str(azimuth))

    # Filter sensor data for the given event_id
    event_sensors = sensor_data_df[sensor_data_df.index == event_id]
    
    x_all = sensor_geometry_df['x'].values
    y_all = sensor_geometry_df['y'].values
    z_all = sensor_geometry_df['z'].values

    # Get event sensor coordinates based on auxiliary option
    if auxiliary:

        auxiliary_sensor_ids = event_sensors[event_sensors['auxiliary'] == True]
        auxiliary_sensor_ids = auxiliary_sensor_ids.drop_duplicates(subset=['sensor_id'])    
        event_sensor_coordinates = sensor_geometry[sensor_geometry.index.isin(auxiliary_sensor_ids['sensor_id'])]
        charges = auxiliary_sensor_ids['charge'].values
        times = auxiliary_sensor_ids['time'].values


    else:
        event_sensors = event_sensors.drop_duplicates(subset=['sensor_id'])
        event_sensor_coordinates = sensor_geometry_df[sensor_geometry_df.index.isin(event_sensors['sensor_id'])]
        charges = event_sensors['charge'].values
        times = event_sensors['time'].values
        print('len charges: '+str(charges.shape))

    charge_min = np.min(charges)
    charge_max = np.max(charges)
    marker_sizes = 5 + (200 * ((charges - charge_min) / (charge_max - charge_min)) ) # Adjust the range of marker sizes as needed

    time_min = np.min(times)
    plottimes = (times - time_min)/1000. # Adjust the range of marker sizes as needed


    print(event_sensor_coordinates['x'].shape, event_sensor_coordinates['y'].shape, event_sensor_coordinates['z'].shape,marker_sizes.shape)
    # Create a 3D plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x_all, y_all, z_all, c='gray', marker='o', s = 1, alpha = .1)

    # Plot the triggered sensors with markers

    colormap = plt.cm.plasma
    plot = ax.scatter(event_sensor_coordinates['x'].values, event_sensor_coordinates['y'].values, event_sensor_coordinates['z'].values, marker='o', s=marker_sizes, c=plottimes, cmap=colormap)


    center_x = np.mean(event_sensor_coordinates['x'].values)
    center_y = np.mean(event_sensor_coordinates['y'].values)
    center_z = np.mean(event_sensor_coordinates['z'].values)

    direction = np.array([
        np.sin(zenith) * np.cos(azimuth),
        np.sin(zenith) * np.sin(azimuth),
        np.cos(zenith)
    ])

    center = np.array([center_x,center_y,center_z])
    arrow_length = 1600
    arrow_center = center - (arrow_length / 2) * direction
    arrow_end = center + (arrow_length / 2) * direction

    # Plot the arrow passing through the center point
    ax.quiver(arrow_center[0], arrow_center[1], arrow_center[2],
            direction[0], direction[1], direction[2], color='red',
            length=arrow_length,arrow_length_ratio=.1)


    cax = fig.add_axes([0.25, 0.87, 0.53, 0.03])  # Adjust the position and size as needed
    cbar = fig.colorbar(plot, cax=cax, orientation='horizontal')
    cax.text(5.5, 1.75, r'Time [$ \mu $s]', ha='center', va='center')

    # cbar = fig.colorbar(plot, ax=ax,shrink=.7)

    # Set labels and title
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_xlim(-600,600)
    ax.set_ylim(-600,600)
    ax.set_zlim(-600,600)
    ax.set_title(f'Neutrino Event {event_id}, Aux = {auxiliary}',loc="center", y=1.18)
    ax.grid(False)


    def rotate(angle):
        ax.view_init(azim=angle)


    rot_animation = FuncAnimation(fig, rotate, frames=np.arange(0,362,1),interval=40)
    rot_animation.save(f'Graphics/{event_id}_rotation.gif', dpi=300, writer='imagemagick')



def angular_dist_score(az_true, zen_true, az_pred, zen_pred):
    '''
    Calculate the MAE of the angular distance between two directions.
    The two vectors are first converted to cartesian unit vectors,
    and then their scalar product is computed, which is equal to
    the cosine of the angle between the two vectors. The inverse 
    cosine (arccos) thereof is then the angle between the two input vectors.
    
    Parameters:
    -----------
    
    az_true : float (or array thereof)
        true azimuth value(s) in radian
    zen_true : float (or array thereof)
        true zenith value(s) in radian
    az_pred : float (or array thereof)
        predicted azimuth value(s) in radian
    zen_pred : float (or array thereof)
        predicted zenith value(s) in radian
    
    Returns:
    --------
    
    dist : float
        mean over the angular distance(s) in radian
    '''

    if not (np.all(np.isfinite(az_true)) and
            np.all(np.isfinite(zen_true)) and
            np.all(np.isfinite(az_pred)) and
            np.all(np.isfinite(zen_pred))):
        raise ValueError("All arguments must be finite")
    
    # pre-compute all sine and cosine values
    sa1 = np.sin(az_true)
    ca1 = np.cos(az_true)
    sz1 = np.sin(zen_true)
    cz1 = np.cos(zen_true)
    
    sa2 = np.sin(az_pred)
    ca2 = np.cos(az_pred)
    sz2 = np.sin(zen_pred)
    cz2 = np.cos(zen_pred)
    
    # scalar product of the two cartesian vectors (x = sz*ca, y = sz*sa, z = cz)
    scalar_prod = sz1*sz2*(ca1*ca2 + sa1*sa2) + (cz1*cz2)
    
    # scalar product of two unit vectors is always between -1 and 1, this is against nummerical instability
    # that might otherwise occure from the finite precision of the sine and cosine functions
    scalar_prod =  np.clip(scalar_prod, -1, 1)
    
    # convert back to an angle (in radian)
    return np.average(np.abs(np.arccos(scalar_prod)))


def avg_angular_dist_score(y_true, y_pred):
    '''
    Take training and validation target datasets and
    split into the training and validation azimuth
    and zenith sets.

    Parameters:
    -----------

    y_true : float (or array thereof)
    y_pred : float (or array thereof)

    Returns:
    --------

    dist : float (or array thereof)
        mean of angular_dist_score scores
    '''


    scores = []
    for i in range(len(y_true)):
        az_true, zen_true = y_true.iloc[i][:2]  # Validation dataset is Pandas dataframe
        az_pred, zen_pred = y_pred[i][:2]       # Predictions are just in a list
        score = angular_dist_score(az_true, zen_true, az_pred, zen_pred)
        scores.append(score)
    return np.mean(scores)
























