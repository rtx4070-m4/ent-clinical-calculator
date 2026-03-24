function calculate_bulk_pta(left::Vector{Float64}, right::Vector{Float64})
    left_avg = sum(left) / length(left)
    right_avg = sum(right) / length(right)
    return (left_avg, right_avg)
end

function vestibular_gain_calc(eye_velocity::Float64, head_velocity::Float64)
    if head_velocity == 0
        return 0.0
    end
    return eye_velocity / head_velocity
end
